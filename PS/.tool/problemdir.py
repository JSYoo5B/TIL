#!/usr/bin/env python3
from os import listdir
from os.path import isdir, isfile, join


def is_problem_dir(path):
    if isdir(path) is False:
        return False
    if isfile(path + 'README.md') is False:
        return False    # Need problem info file.
    if isdir(path + 'testdata/') is False:
        return False    # Need problem input and output data
    
    return True # Finally, path seems problem dir


def get_test_list(path):
    if is_problem_dir(path) is False:
        return None

    d_dir = path + 'testdata/'
    # for all files in testdata/
    d_files = [f for f in listdir(_d_dir) if isfile(join(d_dir, f))]
    # filter *.in and *.out files
    in_files = list(map(lambda x: x.rsplit('.', 1)[0], \
            list(filter(lambda f: f.endswith('.in'), d_files))))
    out_files = list(map(lambda x: x.rsplit('.', 1)[0], \
            list(filter(lambda f: f.endswith('.out'), d_files))))

    # find .in and .out paired names
    return list(filter(lambda t:t in in_files, out_files))
