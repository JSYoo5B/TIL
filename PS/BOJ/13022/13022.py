#!/usr/bin/env python3

import re

if __name__ == '__main__':
    text = input()

    pattern = "(wolf"
    for i in range(2, 13):
        pattern += "|w{}{}{}o{}{}{}l{}{}{}f{}{}{}"\
                .format('{', i, '}','{', i, '}','{', i, '}','{', i, '}',)
    pattern += ")"

    extra = re.sub(pattern, "", text)
    if len(extra) > 0:
        print(0)
    else:
        print(1)

