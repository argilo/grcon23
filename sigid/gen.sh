#!/usr/bin/env bash

set -e

convert \
  -background White \
  -gravity Center \
  -pointsize 15 \
  label:'flag\{paint_all_the_things\}' \
  -rotate 90 \
  -extent x220 \
  -crop 17x220-2+0 \
  -depth 8 \
  gray:freedv_paint_flag.raw
