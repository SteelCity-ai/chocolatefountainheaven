# Chocolate Fountain Heaven — Replit deployment

**Target:** `main` @ `a447d45` · static HTML, no build step, no environment variables, no secrets.
**Web root:** `site/` — the repository root has no `index.html` on purpose.

---

## 1. Import

1. Replit → **Create** → **Import from GitHub** → `SteelCity-ai/chocolatefountainheaven`.
2. Branch: **`main`**. Do not import `codex/STE-355` (the parked design draft).
3. Language/template: **Static** (or "HTML, CSS, JS"). There is nothing to install, compile or generate.

## 2. Run settings

`.replit` is committed and already contains:

```toml
run = "python3 -m http.server 8080 --directory site"

[deployment]
deploymentTarget = "static"
publicDir = "site"

[[ports]]
localPort = 8080
externalPort = 80
```

If the workspace asks instead of using the file, type `python3 -m http.server 8080 --directory site`.

**Do not** set a build command. **Do not** set a start command that expects `server.js`, `npm start` or a framework — there is no server-side code.

## 3. Publish

- Deployment type: **Static**.
- Public directory: **`site`**.
- If the Publishing pane has no "Static" option in your account, choose **Autoscale** and keep the run command above; it serves the same folder.
- Custom domain: add it **after** the name servers are delegated (see `CUTOVER-RUNBOOK.md`). Publishing to a `*.replit.app` URL first is fine and is the recommended smoke test.

## 4. Verify a deploy (2 minutes)

```bash
curl -sI https://<deployed-host>/ | head -1                  # 200
curl -s  https://<deployed-host>/ | grep -c 'hero__slide'    # 5
curl -s  https://<deployed-host>/img/home-2.jpg -o /dev/null -w '%{http_code}\n'   # 200
```

Then check by eye at 1440 px and 390 px: the hero rotates every 4 s on desktop (3 photos) and shows 5 on a phone; the contact form shows 11 fields; the footer has no Greenbrier line.

## 5. What is in the repo (and what is not)

| In `site/` | Count |
|---|---|
| Pages | 7 (`index`, `fountains`, `weddings`, `ranch`, `faq`, `gallery`, `contact`) |
| Stylesheets | 1 |
| Scripts | 1 |
| Images | 26 (hero set with `srcset` variants + gallery) |

Not in the repo: `node_modules`, build artefacts, `.env`, credentials, uploads, Duda exports. `.gitignore` already excludes them.

## 6. Rollback

Static hosting means rollback is a revert, not a migration:

1. Replit → **Deployments** → redeploy the previous build, **or**
2. `git revert <bad-commit> && git push`, then redeploy `main`.

The current live Duda site is untouched until DNS moves, so there is always a working fallback.

---

## In plain English

Replit only has to point at the main branch and the `site` folder. There is nothing to install or build, and no passwords to add. Publish it on the free Replit address first and check a few pages, then connect her real domain once the name servers are handed over. If anything looks wrong, we revert one commit and republish — the old site stays online the whole time.
