# Deployment — review preview

Live review URL: https://cf.steelcity-ai.com

Host: srv1349497 (187.77.6.198)
Static files: /opt/cf-preview/site (copied from site/ in this repo)
Container: cf-web (nginx:alpine, read-only mount, bound to 127.0.0.1:8110)
Traefik: router cf-preview + service cf-preview-svc in /docker/traefik/dynamic.yml
DNS: Cloudflare A record cf.steelcity-ai.com -> 187.77.6.198, DNS-only (not proxied)
TLS: Let's Encrypt via Traefik certResolver letsencrypt

## Update the preview

```
cd site && tar czf - . | ssh -i ~/.ssh/id_ed25519 root@172.18.0.1 \\
  "cd /opt/cf-preview/site && tar xzf -"
```

No container restart is needed; nginx serves the mounted directory.

## Scope

This is a review draft only. The client site https://www.chocolatefountainheaven.com/ is untouched.
Production cutover and DNS move require Mike's approval.
