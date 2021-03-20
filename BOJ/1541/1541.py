#!/usr/bin/env python3

if __name__ == '__main__':
    formula = input()
    polynomials = formula.split('-')
    precalcs = []
    for p in polynomials:
        numbers = list(map(int, p.split('+')))
        if len(precalcs) == 0:
            precalcs.append(sum(numbers))
        else:
            precalcs.append(sum(numbers) * -1)
    
    answer = sum(precalcs)
    print(answer)
        
