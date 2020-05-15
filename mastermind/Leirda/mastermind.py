#!/usr/bin/env python3
import enum


Color = enum.Enum('Color', 'red blue green pink yellow purple')

def hint(secret, guess):
    if secret[0] == guess[0]:
        return [1, 0]
    return [0, 0]