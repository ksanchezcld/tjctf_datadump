#!/bin/bash

curl "https://blank.tjctf.org/" -s |grep -oE "tjctf{.*}" --color=none
