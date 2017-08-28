#!/bin/bash

/opt/vc/bin/raspivid -n -hf -fps 10 -o - -w 320 -h 240 -t 0 | nc.traditional 192.168.100.55 5000
