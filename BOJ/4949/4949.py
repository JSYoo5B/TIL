#!/usr/bin/env python3

def check_parenthesis_pairs(sentence):
    parenthesis = []
    for c in sentence:
        if c == '(' or c == '[':
            parenthesis.append(c)
        elif c == ')' or c == ']':
            if len(parenthesis) == 0:
                return False
            last = parenthesis[-1]
            if (last == '(' and c == ')') or (last == '[' and c == ']'):
                parenthesis.pop()
            else:
                return False
    return len(parenthesis) == 0

if __name__ == '__main__':
    total_input = ''
    while True:
        try:
            last = input()
            if last == '.':
                break;
            total_input += last
        except:
            break

    sentences = total_input.split('.')
    sentences.pop()
    for s in sentences:
        result = check_parenthesis_pairs(s)
        if result:
            print("yes")
        else:
            print("no")
 
