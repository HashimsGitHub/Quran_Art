#!/usr/bin/env bash

set -euo pipefail

BASE_URL="https://quranyusufali.com"
OUTPUT_DIR="quran_html"

mkdir -p "$OUTPUT_DIR"

echo "Downloading home page..."
curl -L -s "$BASE_URL/" -o "$OUTPUT_DIR/index.html"

echo "Downloading Surahs..."

for i in $(seq 1 114); do
    printf "Downloading %3d/114...\n" "$i"
    curl -L -s "${BASE_URL}/${i}/" -o "$OUTPUT_DIR/$(printf "%03d" "$i").html"
done

echo "Done!"