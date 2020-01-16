#!/usr/bin/env python3

from string import whitespace

def is_cjk(char):
    cjk_ranges = [
        {"from": ord(u"\u1100"), "to": ord(u"\u11ff")},
        {"from": ord(u"\uAC00"), "to": ord(u"\uD7AF")},
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


def ends_with_honorics(text):
    honorics = ('Mr', 'Mrs', 'Ms', 'Mx', 'Dr', 'Prof')
    return text.endswith(honorics)


def wrap_text(text, limit_width=80, mdfmt=True):
    if mdfmt:
        soft_wrap = '  \n'
        endl = '\n\n'
    else:
        soft_wrap = '\n'
        endl = '\n'

    res_txt, last_word = '', ''
    line_width, word_width = 0, 0
    for c in text:
        if is_blank_char(c): # When character is blank
            if len(last_word) == 0 or is_blank_char(last_word[-1]):
                # Starts with blank character will be skipped
                # Skip for blank character duplicates
                last_word += ''
            else:
                if line_width + word_width >= limit_width:
                    # When expected line width exceeds, add soft wrap
                    res_txt += soft_wrap + last_word
                    line_width = word_width
                else:
                    last_word += ' '
                    word_width += 1
                    # When expected line width is enough, add in this line
                    res_txt += last_word
                    line_width += word_width
                last_word = ''
                word_width = 0
        elif c == '.': # When character is full-stop
            last_word += '.'
            word_width += 1
            # Check last word was not honorics
            if not ends_with_honorics(last_word[:-1]):
                res_txt += last_word + endl
                line_width = 0
                last_word = ''
                word_width = 0
        else:
            last_word += c
            word_width += 1 + int(is_cjk(c))
    
    return res_txt
