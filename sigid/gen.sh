#!/usr/bin/env bash

set -e

convert \
  -background White \
  -gravity Center \
  -pointsize 15 \
  label:'Flag 1: flag\{paint_all_the_things\}' \
  -rotate 90 \
  -extent x260 \
  -crop 17x260-2+0 \
  -flop \
  -depth 8 \
  gray:freedv_paint_flag.raw

sox part4-flag2.wav --bits 16 --encoding signed-integer --endian little part4-flag2.raw
~/git/codec2/build_linux/src/freedv_tx 1600 part4-flag2.raw freedv.s16
cat <(dd if=/dev/zero bs=2 count=40000) freedv.s16 <(dd if=/dev/zero bs=2 count=40000) > freedv_padded.s16

grcc freedv.grc
./freedv.py
