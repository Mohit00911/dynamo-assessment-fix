#!/bin/bash
set -euo pipefail

mkdir -p /logs/verifier

# pytest is baked into the environment image, alongside pytest-json-ctrf.
# Generate the ctrf.json report in the correct output directory.
pytest /tests/test_outputs.py --json-ctrf /logs/verifier/ctrf.json -rA

# Write the final score to the required verifier directory
if [ $? -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi