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
# One-time setup (system Python is PEP 668-managed, so use a venv):
python3 -m venv .venv
.venv/bin/pip install -r scripts/requirements-local.txt

# Each time the cookie expires:
.venv/bin/python scripts/refresh_cookies.py
```

See [`scripts/refresh_cookies.py`](scripts/refresh_cookies.py) for options (`--browser`,
`--cookie-file`, `--env`, `--repo`). It auto-detects Snap/Flatpak Firefox profiles. This
runs locally only — GitHub's runners have no browser.

### Fully hands-off: the systemd timer

A systemd **user** timer runs the refresh weekly (well ahead of the ~2 week expiry),
inside your logged-in session so `gh`'s keyring-stored token is available, with
`Persistent=true` to catch up if the machine was off. Unit files live in
[`scripts/systemd/`](scripts/systemd/). Install:

```bash
mkdir -p ~/.config/systemd/user
cp scripts/systemd/leetcode-cookie-refresh.{service,timer} ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now leetcode-cookie-refresh.timer
```

Useful checks:

```bash
systemctl --user list-timers leetcode-cookie-refresh.timer   # when it next runs
systemctl --user start leetcode-cookie-refresh.service        # run it now
journalctl --user -u leetcode-cookie-refresh.service          # see output
```

The units assume the repo is at `~/Documents/Projects/leetcode` with the `.venv` created
above. A plain `cron` job does **not** work here — cron has no access to the desktop
keyring where `gh` stores its token.

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
