#!/bin/bash

/opt/vc/bin/raspivid -n -vf -hf -fps 10 -o - -w 320 -h 240 -t 0 | nc.traditional 192.168.100.72 5000
