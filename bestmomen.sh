#!/bin/bash

# Cek apakah token sudah ada di environment variable
if [ -z "${GITHUB_TOKEN+x}" ]; then
    read -s -p "Masukkan Token GitHub: " GITHUB_TOKEN
    echo
fi

URL="https://raw.githubusercontent.com/gorontaloku/linux/main/ubuntu/gaskan.sh"

curl -H "Authorization: token $GITHUB_TOKEN" \
    -sL "$URL" \
    -o gaskan.sh

chmod +x gaskan.sh
./gaskan.sh
