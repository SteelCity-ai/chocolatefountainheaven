#!/usr/bin/env bash
# Publish the local site/ directory to the review preview container (cf-web -> cf.steelcity-ai.com).
# Idempotent copy, no deletions: the preview also keeps design-2/ and design-2-1/ snapshots.
# rsync is not installed in the Hermes container, so this streams a tar over ssh.
set -euo pipefail
SRC="$(cd "$(dirname "$0")/site" && pwd)"
HOST="${CF_PREVIEW_HOST:-root@172.18.0.1}"
DEST="${CF_PREVIEW_DEST:-/opt/cf-preview/site}"
KEY="${CF_SSH_KEY:-/opt/data/.ssh/id_ed25519}"
SSH="ssh -o StrictHostKeyChecking=no -o ConnectTimeout=15 -i $KEY"

tar -czf - -C "$SRC" --exclude=design-2 --exclude=design-2-1 . \
  | $SSH "$HOST" "tar -xzf - -C $DEST && echo EXTRACT_OK"

echo "--- verify"
$SSH "$HOST" "grep -c 'wordmark__mark' $DEST/index.html; grep -c 'Pittsburgh and surrounding areas' $DEST/index.html; grep -c 'img/g07.jpg' $DEST/index.html"
curl -s https://cf.steelcity-ai.com/ | grep -c 'Pittsburgh and surrounding areas'
