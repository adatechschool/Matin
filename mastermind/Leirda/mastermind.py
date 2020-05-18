#!/usr/bin/env python3
import enum


Color = enum.Enum('Color', 'red blue green pink yellow purple')

def hint(secret, guess):
    good = 0
    miss = 0
    for color in zip(guess, secret):
        if color[0] == color[1]:
            good += 1
        elif color[0] in secret:
            miss += 1
    return [good, miss]
