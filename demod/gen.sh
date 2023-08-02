#!/usr/bin/env bash

set -e

SAMP_RATE=480000

grcc ask.grc
python3 ask.py --samp-rate=${SAMP_RATE} --offset=15000

grcc fsk.grc
python3 fsk.py --samp-rate=${SAMP_RATE} --offset=200000

grcc psk.grc
python3 psk.py --samp-rate=${SAMP_RATE} --offset=-140000

grcc impair.grc
python3 impair.py --samp-rate=${SAMP_RATE}
