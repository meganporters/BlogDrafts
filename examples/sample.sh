#!/usr/bin/env bash
set -euo pipefail

python -m sidehustle add "Tiny CLI helper" --tags tools,cli --body "Just testing the flow."
python -m sidehustle list
python -m sidehustle build site

