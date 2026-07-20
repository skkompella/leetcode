#!/usr/bin/env python3
"""Regenerate the repo's README.md with LeetCode stats.

Scans the `solutions/` folder (populated by joshcai/leetcode-sync — one folder
per problem, named like `0001-two-sum`), looks up each problem's difficulty and
topic tags from LeetCode's PUBLIC GraphQL API (no auth), and writes a portfolio
README with:

  - total solved + Easy/Medium/Hard breakdown
  - a table of every solved problem (number, title, difficulty, tags, languages)
  - a per-topic breakdown

Metadata is cached in `.stats-cache.json` so each problem is queried at most once,
keeping the daily CI run fast and polite to LeetCode's rate limiter.

Stdlib only — no pip install needed.
"""

from __future__ import annotations

import json
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOLUTIONS_DIR = REPO_ROOT / "solutions"
CACHE_FILE = REPO_ROOT / ".stats-cache.json"
README_FILE = REPO_ROOT / "README.md"

GRAPHQL_URL = "https://leetcode.com/graphql"
FOLDER_RE = re.compile(r"^(\d+)-(.+)$")

# Map common solution-file extensions to a display language name.
LANG_BY_EXT = {
    ".py": "Python", ".java": "Java", ".cpp": "C++", ".cc": "C++", ".c": "C",
    ".cs": "C#", ".js": "JavaScript", ".ts": "TypeScript", ".go": "Go",
    ".rs": "Rust", ".kt": "Kotlin", ".swift": "Swift", ".rb": "Ruby",
    ".scala": "Scala", ".php": "PHP", ".sql": "SQL", ".sh": "Shell",
    ".ex": "Elixir", ".erl": "Erlang", ".dart": "Dart", ".rkt": "Racket",
}

DIFF_ORDER = {"Easy": 0, "Medium": 1, "Hard": 2}


def load_cache() -> dict:
    if CACHE_FILE.exists():
        try:
            return json.loads(CACHE_FILE.read_text())
        except (json.JSONDecodeError, OSError):
            pass
    return {}


def save_cache(cache: dict) -> None:
    CACHE_FILE.write_text(json.dumps(cache, indent=2, sort_keys=True) + "\n")


def fetch_metadata(slug: str) -> dict | None:
    """Query LeetCode's public GraphQL for a problem's difficulty + topic tags."""
    query = """
    query ($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionFrontendId
        title
        difficulty
        topicTags { name }
      }
    }
    """
    payload = json.dumps({"query": query, "variables": {"titleSlug": slug}}).encode()
    req = urllib.request.Request(
        GRAPHQL_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "leetcode-stats-generator",
            "Referer": f"https://leetcode.com/problems/{slug}/",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read())
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
        print(f"  ! failed to fetch {slug}: {e}", file=sys.stderr)
        return None

    q = (data.get("data") or {}).get("question")
    if not q:
        print(f"  ! no data for {slug}", file=sys.stderr)
        return None
    return {
        "id": q.get("questionFrontendId"),
        "title": q.get("title") or slug.replace("-", " ").title(),
        "difficulty": q.get("difficulty") or "Unknown",
        "tags": [t["name"] for t in (q.get("topicTags") or [])],
    }


def detect_languages(folder: Path) -> list[str]:
    langs = set()
    for f in folder.iterdir():
        if f.is_file():
            lang = LANG_BY_EXT.get(f.suffix.lower())
            if lang:
                langs.add(lang)
    return sorted(langs)


def collect_problems(cache: dict) -> list[dict]:
    if not SOLUTIONS_DIR.is_dir():
        print(f"No solutions folder at {SOLUTIONS_DIR} yet — nothing to do.")
        return []

    problems = []
    for folder in sorted(SOLUTIONS_DIR.iterdir()):
        if not folder.is_dir():
            continue
        m = FOLDER_RE.match(folder.name)
        if not m:
            continue
        slug = m.group(2)

        if slug not in cache:
            print(f"  fetching {slug} ...")
            meta = fetch_metadata(slug)
            if meta is None:
                continue
            cache[slug] = meta
            save_cache(cache)          # persist incrementally — survives partial runs
            time.sleep(0.6)            # be gentle with the rate limiter

        meta = cache[slug]
        problems.append({
            **meta,
            "slug": slug,
            "folder": folder.name,
            "languages": detect_languages(folder),
        })

    # Sort by numeric problem id when available, else by folder number.
    problems.sort(key=lambda p: int(p.get("id") or 0))
    return problems


def render_readme(problems: list[dict]) -> str:
    total = len(problems)
    counts = {"Easy": 0, "Medium": 0, "Hard": 0}
    for p in problems:
        counts[p["difficulty"]] = counts.get(p["difficulty"], 0) + 1

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        "# 🧩 My LeetCode Solutions",
        "",
        "Auto-synced from LeetCode and organized into a portfolio. "
        "Solutions live in [`solutions/`](solutions/); this README is regenerated "
        "on every sync by [`scripts/generate_stats.py`](scripts/generate_stats.py).",
        "",
        "## 📊 Summary",
        "",
        f"**{total} solved** &nbsp;·&nbsp; "
        f"🟢 {counts.get('Easy', 0)} Easy &nbsp;·&nbsp; "
        f"🟡 {counts.get('Medium', 0)} Medium &nbsp;·&nbsp; "
        f"🔴 {counts.get('Hard', 0)} Hard",
        "",
        f"_Last synced: {now}_",
        "",
    ]

    if not problems:
        lines += ["", "_No solutions synced yet — run the workflow to populate this._", ""]
        return "\n".join(lines)

    emoji = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}

    # Main problem table.
    lines += [
        "## ✅ Problems",
        "",
        "| # | Problem | Difficulty | Topics | Languages |",
        "| :-- | :-- | :-- | :-- | :-- |",
    ]
    for p in problems:
        tags = ", ".join(p["tags"]) if p["tags"] else "—"
        langs = ", ".join(p["languages"]) if p["languages"] else "—"
        diff = f"{emoji.get(p['difficulty'], '⚪')} {p['difficulty']}"
        link = f"[{p['title']}](solutions/{p['folder']})"
        lines.append(f"| {p.get('id') or '—'} | {link} | {diff} | {tags} | {langs} |")
    lines.append("")

    # Per-topic breakdown.
    by_tag: dict[str, list[dict]] = {}
    for p in problems:
        for tag in p["tags"]:
            by_tag.setdefault(tag, []).append(p)

    if by_tag:
        lines += ["## 🏷️ By Topic", ""]
        for tag in sorted(by_tag, key=lambda t: (-len(by_tag[t]), t)):
            probs = sorted(by_tag[tag], key=lambda p: int(p.get("id") or 0))
            lines.append(f"<details><summary><b>{tag}</b> ({len(probs)})</summary>")
            lines.append("")
            for p in probs:
                lines.append(f"- [{p.get('id') or '—'}. {p['title']}](solutions/{p['folder']})")
            lines.append("")
            lines.append("</details>")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    cache = load_cache()
    problems = collect_problems(cache)
    save_cache(cache)
    README_FILE.write_text(render_readme(problems))
    print(f"Wrote {README_FILE} ({len(problems)} problems).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
