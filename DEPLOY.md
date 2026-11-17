# Deployment — Chocolate Fountain Heaven

**Hosting: the Steel City AI VPS (srv1349497 / 187.77.6.198). That is the only hosting target for this site.**
Two static nginx containers on that host serve the same repository content: one is the private review preview, one is the production target.

| | Review preview | Production |
|---|---|---|
| URL | https://cf.steelcity-ai.com | `www.chocolatefountainheaven.com` (DNS not yet switched) |
| Web root on host | `/opt/cf-preview/site` | `/opt/cf-prod/site` |
| Container | `cf-web` (`nginx:alpine`, `127.0.0.1:8110`) | `cf-prod` (`nginx:alpine`, `127.0.0.1:8111`) |
| Traefik router | `cf-preview` → `cf-preview-svc` | `cf-prod` + `cf-prod-apex` → `cf-prod-svc` |
| DNS | Cloudflare A → 187.77.6.198 (DNS-only) | Apex + www → 187.77.6.198 **after** the nameserver handover |
| TLS | Let's Encrypt via Traefik | Same, issued on first request after DNS moves |

Both containers mount the site directory read-only and bind to loopback only; Traefik is the only public listener.

## Publish a release (both targets)

```bash
# from the canonical repo, on main
git archive <sha> site | tar -x -C /tmp/cf-release
tar -C /tmp/cf-release/site -czf - . | ssh root@172.18.0.1 \
  "tar -xzf - -C /opt/cf-prod/site"
```

For the preview, use the same command with `/opt/cf-preview/site`.

No container restart is needed; nginx serves the mounted directory. Then compare hashes:

```bash
curl -s https://cf.steelcity-ai.com/index.html | sha256sum
git show <sha>:site/index.html | sha256sum
```

Name the commit, never the URL: a preview can be rebuilt by another task while you are looking at it.

## How the site is built

There is **no build step**. `site/` contains plain HTML, one stylesheet, one script and images. The repository root has no `index.html` on purpose. No environment variables, no secrets, no server-side code.

## Adding a deploy target is not a decision for an agent

The production host, domain and TLS are fixed. Do not add a platform, and do not re-point the domain outside `CUTOVER-RUNBOOK.md`.

## Cutover

See `CUTOVER-RUNBOOK.md` (DNS pre-flight, mail records first, five-minute rollback) and `DNS-HANDOVER.md` (exact records). Production cutover and the DNS move require Mike's approval; the live Duda site is untouched until then.
