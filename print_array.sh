#!/usr/bin/env bash
if [ $# -ne "1" ]; then
    echo "Usage: $0 <index as written in the code>"
fi
cat ./permuted_array.txt | tail -n +$(($1 - 0x19b +1)) | head -n 1 | tr -d ' \t'
