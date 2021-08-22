#!/usr/bin/env python3
from itertools import zip_longest
from subprocess import Popen, PIPE, TimeoutExpired
from time import time
import os
import sys

def get_terminal_width():
    try:
        col, row = os.get_terminal_size(0)
    except OSError:
        col, row = os.get_terminal_size(1)
    return col


def format_single_line(exp, act, width):
    to_line = lambda x, w: '-'.center(w, '-') if x == None else ' ' + x

    if exp == act:
        line = '===' + to_line(exp, width - 4)
    else:
        line = 'EXP' + to_line(exp, width - 4)
        line += '\nACT' + to_line(act, width - 4)

    return line


def format_compare_line(exp, act, width):
    to_line = lambda x, w: '-'.center(w, '-') if x == None else ' ' + x

    line = '{0:<{1}}'.format(to_line(exp, width), width)
    if exp == act:
        line += '|'
    else:
        line += 'X'
    line += '{0:<{1}}'.format(to_line(act, width), width)

    return line


def print_compare(expect, actual):
    exp_lines = expect.splitlines()
    act_lines = actual.splitlines()
    
    all_lines = exp_lines + act_lines
    line_width = max(20, len(max(all_lines, key=len)))
    term_width = get_terminal_width()

    if line_width * 2 > term_width - 5:
        print_width = term_width
        header_line = ' Expected and actual '.center(print_width, '=')
        format_line = format_single_line
        footer_line = '='.center(print_width, '=')
    else:
        print_width = line_width + 2
        header_line = ' Expected '.center(print_width, '=') + '|' \
                + ' Actual '.center(print_width, '=')
        format_line = format_compare_line
        footer_line = '='.center(print_width, '=') + '|' \
                + '='.center(print_width, '=') 

    print(header_line)
    for (exp, act) in zip_longest(exp_lines, act_lines):
        print(format_line(exp, act, print_width))
    print(footer_line)


def test_solution(path, exe, testname, to):
    in_path = path + 'testdata/' + testname + '.in'
    out_path = path + 'testdata/' + testname + '.out'

    with open(in_path, 'r') as in_file, open(out_path, 'r') as out_file:
        proc = Popen([exe], stdin=PIPE, stdout=PIPE)

        print('=== Testing ' + testname)
        in_data = in_file.read().encode()
        start_time = time()
        try :
            outs, errs = proc.communicate(input=in_data, timeout=to)
            time_elapsed = time() - start_time
            
            expect = out_file.read()
            actual = outs.decode('ascii')
            if expect == actual:
                print('=== Test passed in {:.3f}sec'.format(time_elapsed))
                passed = True
            else:
                print('=== Test failed: incorrect answer')
                print_compare(expect, actual)
                passed = False

        except TimeoutExpired:
            proc.kill()
            print('=== Test failed: timeout (limit: {}sec)'.format(to))
            passed = False

    return passed
