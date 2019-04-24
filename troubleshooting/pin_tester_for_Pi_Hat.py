#!/usr/bin/env python3
from RPi.GPIO import *
import sys,time

def test(what):
    setmode(BOARD)
    setwarnings(False)
    setup(what, OUT)
    if input(what) == 0:
        output(what,HIGH)
    else:
        output(what,LOW)

if __name__ == '__main__':
    if sys.argv[1] == 'i':
        test(int(sys.argv[2]))
        time.sleep(1)
        test(int(sys.argv[2]))
    else:
        bad = [1, 2, 4, 6, 9, 14, 17, 20, 25, 27, 28, 30, 33, 34, 39]
        for i in range(1,41):
            if i not in bad:
                print(i)
                test(i)
                time.sleep(float(sys.argv[1]))
                test(i)

