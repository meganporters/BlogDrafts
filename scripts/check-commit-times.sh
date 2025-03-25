#!/usr/bin/env bash
set -euo pipefail

git --no-pager log --pretty=format:'%h %ad %an %s' --date=iso | sed -n '1,30p'

