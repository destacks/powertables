#!/usr/bin/env bash

set -e

./format_code.sh

exec git -c core.fileMode=false diff --exit-code
