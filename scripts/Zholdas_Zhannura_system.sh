#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
printf '%s\n' '==============================' 'Student Information' '=============================='
printf '%s\n' 'Name: Zhannura' 'Surname: Zholdas' 'Group: IT2-2306' 'Student ID: 37742'
printf '\n%s\n' '==============================' 'System Information' '=============================='
printf 'Username: '; whoami
printf 'Hostname: '; hostname
printf 'Current Date: '; date --iso-8601=seconds
printf 'Operating System: '; uname -a
printf '\nDisk Usage:\n'; df -h /
printf '\nMemory Usage:\n'; free -h
if [[ -f "$ROOT/Zholdas_Zhannura_info.txt" ]]; then
  echo 'Student information file exists.'
else
  echo 'Student information file does not exist.'
fi
