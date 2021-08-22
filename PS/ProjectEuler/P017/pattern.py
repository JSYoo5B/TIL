#!/usr/bin/env python3
""" Using number patterns
1. 1 ~ 19: unique words
2. 20 ~ 90: unique words
3. 21 ~ 99: (20 ~ 90) + (1 ~ 9)
4. 100 ~ 900: (1 ~ 9) + hundread
5. 101 ~ 999: (100 ~ 900) + and + (1 ~ 99)
6. 1000: hundread
"""

num_letters = [0 for i in range(0,1001)]

if __name__ == '__main__':
    # Set unique words (1 ~ 19)
    letters_1_10 = ['one', 'two', 'three', 'four', 'five',
            'six', 'seven', 'eight', 'nine', 'ten']
    letters_11_19 = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
            'sixteen', 'seventeen', 'eighteen', 'nineteen']
    num_letters[1:10] = [len(l) for l in letters_1_10]
    num_letters[11:19] = [len(l) for l in letters_11_19]
   
    # Set unique words (20 ~ 90)
    num_letters[20] = len('twenty')
    num_letters[30] = len('thirty')
    num_letters[40] = len('forty')
    num_letters[50] = len('fifty')
    num_letters[60] = len('sixty')
    num_letters[70] = len('seventy')
    num_letters[80] = len('eighty')
    num_letters[90] = len('ninety')
    # Set 21 ~ 99
    for n in range(21, 99+1):
        if num_letters[n] != 0:
            continue
        num_letters[n] = num_letters[int(n / 10) * 10] + num_letters[n % 10]
    
    # Set 100 ~ 900
    for n in range(100, 900+1, 100):
        num_letters[n] = num_letters[int(n / 100)] + len('hundred')
    # Set 101 ~ 999
    for n in range(101, 999+1):
        if num_letters[n] != 0:
            continue
        num_letters[n] = num_letters[int(n / 100) * 100] \
                + len('and') + num_letters[n % 100]

    # Set unique word (1000)
    num_letters[1000] = len('onethousand')

    answer = sum(num_letters)
    print(answer)
