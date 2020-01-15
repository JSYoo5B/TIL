#!/usr/bin/env python3

from string import whitespace

def is_cjk(char):
    cjk_ranges = [
        {"from": ord(u"\u3300"), "to": ord(u"\u33ff")},
        {"from": ord(u"\ufe30"), "to": ord(u"\ufe4f")},
        {"from": ord(u"\uf900"), "to": ord(u"\ufaff")},
        {"from": ord(u"\U0002F800"), "to": ord(u"\U0002fa1f")},
        {'from': ord(u'\u3040'), 'to': ord(u'\u309f')},
        {"from": ord(u"\u30a0"), "to": ord(u"\u30ff")},
        {"from": ord(u"\u2e80"), "to": ord(u"\u2eff")},
        {"from": ord(u"\u4e00"), "to": ord(u"\u9fff")},
        {"from": ord(u"\u3400"), "to": ord(u"\u4dbf")},
        {"from": ord(u"\U00020000"), "to": ord(u"\U0002a6df")},
        {"from": ord(u"\U0002a700"), "to": ord(u"\U0002b73f")},
        {"from": ord(u"\U0002b740"), "to": ord(u"\U0002b81f")},
        {"from": ord(u"\U0002b820"), "to": ord(u"\U0002ceaf")}
    ]

    return any([r["from"] <= ord(char) <= r["to"] for r in cjk_ranges])

def is_blank_char(char):
    return char in whitespace


def is_honoric_expr(text):
    honorics = ['Mr', 'Mrs', 'Ms', 'Mx', 'Dr', 'Prof']
    return text in honorics

