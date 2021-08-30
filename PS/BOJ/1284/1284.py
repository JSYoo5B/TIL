#!/usr/bin/env python3

if __name__ == '__main__':
    while True:
        number = input()
        if number == '0':
            break
        # spaces between numbers
        width = len(number) + 1
        for i in number:
            if i == '0':
                width += 4
            elif i == '1':
                width += 2
            else:
                width += 3
        print(width)
