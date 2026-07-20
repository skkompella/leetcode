#!/usr/bin/env python3
"""Fetch accepted LeetCode submissions and write them into `solutions/`.

Replaces the abandoned joshcai/leetcode-sync action with our own fetcher built on
LeetCode's stable REST endpoint `https://leetcode.com/api/submissions/`, which returns
each submission's full source code directly.

Design goals:
  - **Incremental**: remembers the newest submission timestamp in `.sync-state.json` and
    stops paging once it reaches already-synced submissions, so daily runs are cheap.
    First run (no state) back-fills everything.
  - **Clear failures**: an expired/invalid cookie exits non-zero with a plain-English
    message (the workflow goes red) instead of a cryptic crash.
  - **Portfolio layout**: writes `solutions/<frontendId>-<slug>/<slug>.<ext>`, matching
    what scripts/generate_stats.py expects. Frontend problem numbers come from LeetCode's
    PUBLIC GraphQL and are cached in `.stats-cache.json` (shared with the stats script).

Auth: reads env vars LEETCODE_SESSION and LEETCODE_CSRF_TOKEN (set as GitHub secrets).
Stdlib only — no pip install needed.
"""

from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOLUTIONS_DIR = REPO_ROOT / "solutions"
CACHE_FILE = REPO_ROOT / ".stats-cache.json"     # shared with generate_stats.py
STATE_FILE = REPO_ROOT / ".sync-state.json"

BASE = "https://leetcode.com"
SUBMISSIONS_URL = BASE + "/api/submissions/?offset={offset}&limit={limit}"
GRAPHQL_URL = BASE + "/graphql"
PAGE_LIMIT = 20
MAX_PAGES = 500          # safety cap (~10k submissions); logged if hit
PAGE_SLEEP = 1.0         # be gentle with the rate limiter

# LeetCode `lang` slug -> file extension.
EXT_BY_LANG = {
    "python": ".py", "python3": ".py", "pythondata": ".py",
    "cpp": ".cpp", "c": ".c", "java": ".java", "csharp": ".cs",
    "javascript": ".js", "typescript": ".ts", "golang": ".go", "go": ".go",
    "rust": ".rs", "kotlin": ".kt", "swift": ".swift", "ruby": ".rb",
    "scala": ".scala", "php": ".php", "racket": ".rkt", "erlang": ".erl",
    "elixir": ".ex", "dart": ".dart", "bash": ".sh",
    "mysql": ".sql", "mssql": ".sql", "oraclesql": ".sql", "postgresql": ".sql",
}


def die(msg: str) -> "None":
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def load_dotenv(path: Path = REPO_ROOT / ".env") -> None:
    """Populate os.environ from a local .env file for local runs.

    Does NOT override variables already set in the environment, so CI's real
    secrets always win over anything on disk.
    """
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        os.environ.setdefault(key.strip(), val.strip().strip('"').strip("'"))


def get_credentials() -> tuple[str, str]:
    session = os.environ.get("LEETCODE_SESSION", "").strip()
    csrf = os.environ.get("LEETCODE_CSRF_TOKEN", "").strip()
    if not session or not csrf:
        die("LEETCODE_SESSION and LEETCODE_CSRF_TOKEN must be set (as repo secrets).")
    return session, csrf


def auth_headers(session: str, csrf: str) -> dict:
    return {
        "Cookie": f"LEETCODE_SESSION={session}; csrftoken={csrf}",
        "x-csrftoken": csrf,
        "Referer": BASE + "/submissions/",
        "Origin": BASE,
        "Content-Type": "application/json",
        # A browser-like UA avoids some Cloudflare edge blocks.
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
        ),
    }


def load_json(path: Path, default):
    if path.exists():
        try:
            return json.loads(path.read_text())
        except (json.JSONDecodeError, OSError):
            pass
    return default


def save_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")


def fetch_page(offset: int, headers: dict) -> dict:
    url = SUBMISSIONS_URL.format(offset=offset, limit=PAGE_LIMIT)
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        if e.code in (401, 403):
            die("LeetCode rejected the credentials (HTTP %d). Your LEETCODE_SESSION "
                "cookie has most likely expired — grab a fresh one and update the "
                "repo secrets (see SETUP.md)." % e.code)
        die(f"HTTP {e.code} fetching submissions: {e.reason}")
    except (urllib.error.URLError, TimeoutError) as e:
        die(f"Network error fetching submissions: {e}")

    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        # LeetCode returns an HTML login/Cloudflare page instead of JSON when unauthorized.
        snippet = raw[:200].replace("\n", " ")
        die("Expected JSON but got HTML — the session is probably invalid or "
            f"blocked. First 200 chars: {snippet!r}")
    if "submissions_dump" not in data:
        die(f"Unexpected response shape (keys: {list(data)}). "
            "The session may be invalid.")
    return data


def fetch_frontend_meta(slug: str, cache: dict) -> dict:
    """Public GraphQL: frontend problem number + difficulty + tags. Cached per slug."""
    if slug in cache:
        return cache[slug]
    query = ("query($s:String!){question(titleSlug:$s){questionFrontendId title "
             "difficulty topicTags{name}}}")
    payload = json.dumps({"query": query, "variables": {"s": slug}}).encode()
    req = urllib.request.Request(
        GRAPHQL_URL, data=payload,
        headers={"Content-Type": "application/json", "User-Agent": "leetcode-sync"},
    )
    meta = {"id": None, "title": slug.replace("-", " ").title(),
            "difficulty": "Unknown", "tags": []}
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            q = (json.loads(resp.read()).get("data") or {}).get("question") or {}
        meta = {
            "id": q.get("questionFrontendId"),
            "title": q.get("title") or meta["title"],
            "difficulty": q.get("difficulty") or "Unknown",
            "tags": [t["name"] for t in (q.get("topicTags") or [])],
        }
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
        print(f"  ! metadata lookup failed for {slug}: {e}", file=sys.stderr)
    cache[slug] = meta
    save_json(CACHE_FILE, cache)
    time.sleep(0.4)
    return meta


def folder_name(meta: dict, slug: str) -> str:
    num = meta.get("id")
    prefix = str(num).zfill(4) if num else "0000"
    return f"{prefix}-{slug}"


def main() -> int:
    load_dotenv()
    session, csrf = get_credentials()
    headers = auth_headers(session, csrf)
    cache = load_json(CACHE_FILE, {})
    state = load_json(STATE_FILE, {})
    last_synced_ts = int(state.get("last_timestamp", 0))

    SOLUTIONS_DIR.mkdir(exist_ok=True)

    # Collect newest-first, keeping only the latest accepted submission per (slug, lang).
    best: dict[tuple[str, str], dict] = {}
    max_ts = last_synced_ts
    reached_known = False

    for page in range(MAX_PAGES):
        data = fetch_page(page * PAGE_LIMIT, headers)
        dump = data.get("submissions_dump") or []
        if not dump:
            break
        for sub in dump:
            ts = int(sub.get("timestamp") or 0)
            max_ts = max(max_ts, ts)
            if ts <= last_synced_ts:
                reached_known = True          # everything from here down is already synced
                continue
            if sub.get("status_display") != "Accepted":
                continue
            slug = sub.get("title_slug")
            lang = sub.get("lang")
            if not slug or not lang:
                continue
            key = (slug, lang)
            if key not in best or ts > int(best[key].get("timestamp") or 0):
                best[key] = sub
        print(f"  page {page}: {len(dump)} submissions "
              f"(new accepted so far: {len(best)})")
        if reached_known or not data.get("has_next"):
            break
        time.sleep(PAGE_SLEEP)
    else:
        print(f"  ! reached MAX_PAGES={MAX_PAGES}; some old submissions may be skipped.")

    if not best:
        print("No new accepted submissions since last sync. Nothing to write.")
        if max_ts > last_synced_ts:
            save_json(STATE_FILE, {"last_timestamp": max_ts})
        return 0

    written = 0
    for (slug, lang), sub in sorted(best.items()):
        code = sub.get("code")
        if not code:
            print(f"  ! no code for {slug} ({lang}); skipping", file=sys.stderr)
            continue
        meta = fetch_frontend_meta(slug, cache)
        folder = SOLUTIONS_DIR / folder_name(meta, slug)
        folder.mkdir(parents=True, exist_ok=True)
        ext = EXT_BY_LANG.get(lang, ".txt")
        dest = folder / f"{slug}{ext}"
        new_content = code if code.endswith("\n") else code + "\n"
        if dest.exists() and dest.read_text() == new_content:
            continue                          # unchanged; avoid needless churn
        dest.write_text(new_content)
        written += 1
        print(f"  wrote {dest.relative_to(REPO_ROOT)}")

    save_json(STATE_FILE, {"last_timestamp": max_ts})
    print(f"Done. Wrote/updated {written} solution file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
