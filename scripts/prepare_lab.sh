#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
mkdir -p "$ROOT/logs" "$ROOT/backup"
cat > "$ROOT/logs/application.log" <<'EOF'
INFO Application started
INFO User logged in
WARNING Configuration file missing
INFO Database connected
ERROR Database connection failed
INFO Application restarted
WARNING Memory usage is high
INFO Request received
ERROR Request failed
INFO Application stopped
EOF
chmod 600 "$ROOT/private.txt"
chmod 644 "$ROOT/public.txt"
chmod +x "$ROOT"/scripts/*.sh
