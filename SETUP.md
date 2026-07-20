# Setup (one-time, ~10 minutes)

Everything runs on GitHub's servers on a daily cron. You only need to do these steps once.

## 1. Create the public repo

Create a new **public** GitHub repo (e.g. `leetcode`) and push these files to it:

```bash
cd leetcode
git init
git add .
git commit -m "Initial commit: LeetCode sync + stats"
git branch -M main
git remote add origin git@github.com:<your-username>/leetcode.git
git push -u origin main
```

## 2. Grab your LeetCode cookies

1. Log in at <https://leetcode.com>.
2. Open DevTools (F12) → **Application** tab → **Cookies** → `https://leetcode.com`
   (or the **Network** tab → click any `leetcode.com` request → **Request Headers → cookie**).
3. Copy two values:
   - **`LEETCODE_SESSION`** — a long token
   - **`csrftoken`** — a shorter token

## 3. Add them as repo secrets

Repo → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**:

| Secret name           | Value                        |
| --------------------- | ---------------------------- |
| `LEETCODE_SESSION`    | the `LEETCODE_SESSION` value |
| `LEETCODE_CSRF_TOKEN` | the `csrftoken` value        |

(`github-token` is provided automatically — no secret needed.)

## 4. Run it

Repo → **Actions** tab → **Sync LeetCode** → **Run workflow**.
Don't wait for the daily cron — trigger it manually the first time.

- The first run **back-fills** all your historical accepted submissions into `solutions/`
  (it pages through your whole submission history). Later runs are incremental — they
  remember the newest timestamp in `.sync-state.json` and only pull what's new.
- After that, it runs daily at 08:00 UTC and only commits when you've solved something new.

## Maintenance: the one recurring chore

The `LEETCODE_SESSION` cookie expires every **~2–4 weeks**. When it does, the daily run
fails with a clear message (`ERROR: ... cookie has most likely expired`).

**One-command fix** (reads the cookie from your logged-in Firefox and updates the GitHub
secret automatically — no DevTools, no copy-paste):

```bash
pip install -r scripts/requirements-local.txt   # once
python3 scripts/refresh_cookies.py               # each time the cookie expires
```

See [`scripts/refresh_cookies.py`](scripts/refresh_cookies.py) for options (`--browser`,
`--env`, `--repo`). This runs locally only — GitHub's runners have no browser. Point a
local cron/systemd timer at it to make refreshing fully hands-off.

**Manual fallback:** repeat steps 2–3 above with a fresh cookie value, then re-run the
workflow from the Actions tab.

_Optional later:_ add a step that opens a GitHub issue / sends a notification on failure so
you get pinged when the cookie dies instead of noticing a red X.

## Tweaks

- **Schedule:** edit the `cron` line in [`.github/workflows/sync-leetcode.yml`](.github/workflows/sync-leetcode.yml).
  `0 8 * * *` = daily 08:00 UTC. (`0 8 * * 6` = weekly Saturdays.)
- **Fetcher:** [`scripts/sync_submissions.py`](scripts/sync_submissions.py) pulls from
  LeetCode's `/api/submissions/` endpoint and writes `solutions/<id>-<slug>/<slug>.<ext>`.
- **Stats:** [`scripts/generate_stats.py`](scripts/generate_stats.py) is yours to hack —
  add a streak heatmap, per-language totals, etc.
