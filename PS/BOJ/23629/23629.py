#!/usr/bin/env python3

import re

if __name__ == '__main__':
    formula = input()
    origin_formula = formula.replace("ONE", "1").replace("TWO", "2")\
            .replace("THREE", "3").replace("FOUR", "4").replace("FIVE", "5")\
            .replace("SIX", "6").replace("SEVEN", "7").replace("EIGHT", "8")\
            .replace("NINE", "9").replace("ZERO", "0")
    inval_token = [ u for u in re.findall(r"[A-Z]", origin_formula) if len(u) > 0 ]
    if len(inval_token) > 0:
        numbers = [0]
        ops = []
    else:
        numbers = [ int(n) for n in re.split(r"[+\-x/]", origin_formula[:-1]) if len(n) > 0 ]
        ops = [ o for o in re.split(r"[\d]", origin_formula[:-1]) if len(o) > 0 ]
    
    result = numbers[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            result += numbers[i+1]
        elif ops[i] == '-':
            result -= numbers[i+1]
        elif ops[i] == 'x':
            result *= numbers[i+1]
        elif ops[i] == '/':
            absol = abs(result) // abs(numbers[i+1])
            if result != 0:
                sign = (result * numbers[i+1]) // (abs(result) * abs(numbers[i+1]))
            else:
                sign = 0
            result = sign * absol
        else:
            inval_token.append(ops[i])
            break
    if len(inval_token) > 0:
        print("Madness!")
    else:
        print(origin_formula)
        stringify = str(result).replace("1", "ONE").replace("2", "TWO")\
                .replace("3", "THREE").replace("4", "FOUR").replace("5", "FIVE")\
                .replace("6", "SIX").replace("7", "SEVEN").replace("8", "EIGHT")\
                .replace("9", "NINE").replace("0", "ZERO")
        print(stringify)
