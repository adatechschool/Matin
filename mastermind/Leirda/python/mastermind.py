#!/usr/bin/env python3
import enum


Color = enum.Enum('Color', 'red blue green black white pink')

def hint(secret, guess):
    good, miss = 0, 0
    for guess_peg, secret_peg in list(zip(guess, secret)):
        if guess_peg == secret_peg:
            good += 1
        elif guess_peg in secret:
            secret.remove(guess_peg)
            miss += 1
    return good, miss

def hint(secret, guess):
    good, miss = 0, 0
    for guess_peg, secret_peg in zip(guess, secret):
        if guess_peg in secret:
            if guess_peg == secret_peg:
                good += 1
            else:
                miss += 1
