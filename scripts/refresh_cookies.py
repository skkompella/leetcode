#!/usr/bin/env python3
"""Refresh LeetCode cookies from your local browser and push them to GitHub secrets.

LOCAL-ONLY helper (this does NOT run in CI — GitHub's runners have no browser).
It reads `LEETCODE_SESSION` + `csrftoken` from a local browser where you're already
logged into LeetCode, verifies they actually work, then updates the repo's GitHub
Actions secrets via `gh secret set` so the daily cloud sync always has a fresh cookie.

Turns the ~monthly "cookie expired" chore into one command:

    python3 scripts/refresh_cookies.py

Requirements:
  - pip install browser_cookie3
  - gh CLI installed and authenticated (`gh auth login`)

Options:
  --repo OWNER/NAME   Target repo (default: auto-detected from the git remote)
  --browser NAME      firefox (default) | chrome | chromium | brave | edge
  --env               Also write the values into the local .env file
  --no-verify         Skip the live check against LeetCode before pushing
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = REPO_ROOT / ".env"
SUBMISSIONS_URL = "https://leetcode.com/api/submissions/?offset=0&limit=1"


def die(msg: str) -> "None":
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def detect_repo() -> str | None:
    """Parse OWNER/NAME from the git remote (handles SSH and HTTPS URLs)."""
    try:
        url = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "config", "--get", "remote.origin.url"],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    m = re.search(r"github\.com[:/]([^/]+/[^/]+?)(?:\.git)?$", url)
    return m.group(1) if m else None


def read_cookies(browser: str) -> dict:
    try:
        import browser_cookie3
    except ImportError:
        die("browser_cookie3 is not installed. Run:  pip install browser_cookie3")

    loaders = {
        "firefox": browser_cookie3.firefox,
        "chrome": browser_cookie3.chrome,
        "chromium": browser_cookie3.chromium,
        "brave": browser_cookie3.brave,
        "edge": browser_cookie3.edge,
    }
    loader = loaders.get(browser)
    if loader is None:
        die(f"Unknown browser {browser!r}. Choose from: {', '.join(loaders)}")

    try:
        jar = loader(domain_name="leetcode.com")
    except Exception as e:  # browser_cookie3 raises assorted errors per platform
        die(f"Could not read {browser} cookies: {e}\n"
            "Make sure you're logged into leetcode.com in that browser "
            "(for Chrome-family browsers, try closing the browser first).")
    return {c.name: c.value for c in jar}


def verify(session: str, csrf: str) -> None:
    req = urllib.request.Request(
        SUBMISSIONS_URL,
        headers={
            "Cookie": f"LEETCODE_SESSION={session}; csrftoken={csrf}",
            "x-csrftoken": csrf,
            "Referer": "https://leetcode.com/submissions/",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) leetcode-refresh",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        if e.code in (401, 403):
            die("The browser cookie is present but LeetCode rejected it "
                f"(HTTP {e.code}). Log into leetcode.com in your browser again, "
                "then re-run.")
        die(f"HTTP {e.code} while verifying: {e.reason}")
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
        die(f"Could not verify the cookie against LeetCode: {e}")
    if "submissions_dump" not in data:
        die("Cookie did not authenticate (no submission data returned).")
    print("  ✓ verified against LeetCode")


def push_secret(name: str, value: str, repo: str) -> None:
    # Pass the value via stdin so it never appears in the process argument list.
    try:
        subprocess.run(
            ["gh", "secret", "set", name, "--repo", repo],
            input=value, text=True, check=True, capture_output=True,
        )
    except FileNotFoundError:
        die("gh CLI not found. Install it and run `gh auth login`.")
    except subprocess.CalledProcessError as e:
        die(f"gh secret set {name} failed: {e.stderr.strip()}")
    print(f"  ✓ updated GitHub secret {name} on {repo}")


def write_env(session: str, csrf: str) -> None:
    ENV_FILE.write_text(
        "# Local secrets — gitignored, never committed. "
        "Managed by scripts/refresh_cookies.py.\n"
        f"LEETCODE_SESSION={session}\n"
        f"LEETCODE_CSRF_TOKEN={csrf}\n"
    )
    print(f"  ✓ wrote {ENV_FILE.relative_to(REPO_ROOT)}")


def main() -> int:
    ap = argparse.ArgumentParser(description="Refresh LeetCode cookies into GitHub secrets.")
    ap.add_argument("--repo", help="Target repo OWNER/NAME (default: auto-detect).")
    ap.add_argument("--browser", default="firefox",
                    help="Browser to read cookies from (default: firefox).")
    ap.add_argument("--env", action="store_true", help="Also write the local .env file.")
    ap.add_argument("--no-verify", action="store_true",
                    help="Skip the live LeetCode check before pushing.")
    args = ap.parse_args()

    repo = args.repo or detect_repo()
    if not repo:
        die("Could not detect the repo. Pass --repo OWNER/NAME.")

    print(f"Reading LeetCode cookies from {args.browser} ...")
    cookies = read_cookies(args.browser)
    session = cookies.get("LEETCODE_SESSION")
    csrf = cookies.get("csrftoken")
    if not session or not csrf:
        die("Did not find LEETCODE_SESSION and csrftoken cookies. "
            "Log into leetcode.com in your browser first.")
    print(f"  ✓ found cookies (session {len(session)} chars, csrf {len(csrf)} chars)")

    if not args.no_verify:
        verify(session, csrf)

    push_secret("LEETCODE_SESSION", session, repo)
    push_secret("LEETCODE_CSRF_TOKEN", csrf, repo)
    if args.env:
        write_env(session, csrf)

    print("Done. The daily sync will use the refreshed cookie.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
