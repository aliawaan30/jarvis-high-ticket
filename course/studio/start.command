#!/bin/bash
# Double click this to open the studio.
cd "$(dirname "$0")"
python3 server.py 4330 &
sleep 1
open "http://127.0.0.1:4330/"
wait
