#!/usr/bin/env python3

import re

if __name__ == '__main__':
    formula = input()
    terms = [ t for t in re.findall(r"[+-]?\d*x*", formula) if len(t) > 0 ]
    integ_formula = ""
    for t in terms:
        degree = t.count('x')
        coeff = t.split('x')[0]
        degree += 1
        try:
            coeff = int(coeff)
        except:
            coeff = int(coeff + '1')
        coeff //= degree
        if len(integ_formula) == 0 and coeff > 0:
            pass
        elif coeff > 0:
            integ_formula += '+'
        elif coeff < 0:
            integ_formula += '-'
        else:
            continue
        if abs(coeff) != 1:
            integ_formula += str(abs(coeff))
        integ_formula += ''.join(['x' for _ in range(degree)])

    if len(integ_formula) > 0:
        integ_formula += '+'
    integ_formula += "W"
    print(integ_formula)
