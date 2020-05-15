#!/usr/bin/env python


cp = input("Proposez un code composé de 2 chiffres allant de 1 à 2.\n")
code = [1, 2]

cbp = 0
cmp = 0

for i in range(0, len(code)):
    if code[i] == cp[i]:
        cbp += 1
    if code[i] in cp[:i] + cp[i+1:]:
        cmp += 1

print("Nombre de chiffre(s) bien placé(s):", cbp)
print("Nombre de chiffre(s) mal placé(s):", cmp)
