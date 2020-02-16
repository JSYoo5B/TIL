#!/usr/env/python3
""" Bruteforce
1.  Loop each two numbers from 999 to 100
2.  Generate product number
3.  Check palindrome
    1)  Convert number into string
    2)  Generate reverse-ordered string
    3)  Compare normal-ordered and reverse-ordered
"""

def is_palindrome(num):
    num_str = str(num)

    rev = "".join(reversed(num_str))

    return num_str == rev

if __name__ == '__main__':
    num1 = 999
    LIMIT = 100

    stop = False
    for i in range(num1, LIMIT, -1):
        for j in range(i, LIMIT, -1):
            if is_palindrome(i * j):
                print(i * j)
                stop = True
                break
        if stop:
            break

