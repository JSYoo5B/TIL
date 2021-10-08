#!/usr/bin/env python3

if __name__ == '__main__':
    expr = input()
    test = expr.replace("+","&").replace("-","&").replace("/","&").replace("*","&")
    expr = expr.replace("/", "//")
    try:
        eval(test)
        answer = int(eval(expr))
        print(answer)
    except:
        print("ROCK")
