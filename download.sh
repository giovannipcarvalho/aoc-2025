#!/usr/bin/env bash

# usage: ./download.sh 1
# downloads input for day 1 as `input.txt` in the current folder
# SESSION environment variable must be set to the advent of code session cookie

set -eu
. .env
curl \
    -A "giovannipcarvalho via curl" \
    -H "cookie: session=${SESSION}" \
    -sSLo day$(printf '%02d' $1)/input.txt \
    https://adventofcode.com/2025/day/$1/input

head day$(printf '%02d' $1)/input.txt
