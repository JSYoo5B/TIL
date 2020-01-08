#!/usr/bin/env python3
from subprocess import Popen, PIPE, TimeoutExpired
from time import time


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
                print('===== Expected')
                print(expect)
                print('===== Actual')
                print(actual)
                passed = False

        except TimeoutExpired:
            proc.kill()
            print('=== Test failed: timeout (limit: {}sec)'.format(to))
            passed = False

    return passed
