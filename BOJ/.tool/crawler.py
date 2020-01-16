#!/usr/bin/env python3
from subprocess import Popen, PIPE
from textformatter import wrap_text
import os


def get_problem_info(lines):
    # TODO: need to change start index identifier
    start = [ln.strip() for ln in lines].index('+ [53]강의 요청하기')
    end = [ln for ln in lines].index('힌트')
    
    # Check index for problem info
    prob_lines = lines[start + 1:end]
    title = prob_lines[1].strip()
    state_stx = [ln for ln in prob_lines].index('문제')
    in_stx = [ln for ln in prob_lines].index('입력')
    out_stx = [ln for ln in prob_lines].index('출력')
    exin_stx = [ln for ln in prob_lines].index('예제 입력 1 (BUTTON) 복사')
    exout_stx = [ln for ln in prob_lines].index('예제 출력 1 (BUTTON) 복사')
    
    # Extract table data
    table_tok = prob_lines[4].split()
    prob_table = [ table_tok[0] + ' ' + table_tok[1], \
                    table_tok[2] + ' ' + table_tok[3] ]

    # Extract problem info strings
    del_indent = lambda x: x[len('   '):]
    state_lines = list(map(del_indent, prob_lines[state_stx + 2: in_stx - 1]))
    input_lines = list(map(del_indent, prob_lines[in_stx + 2: out_stx - 1]))
    output_lines = list(map(del_indent, prob_lines[out_stx + 2: exin_stx - 1]))
    # TODO: add more ex in and ex out
    exin_lines = prob_lines[exin_stx + 2: exout_stx - 1]
    exout_lines = prob_lines[exout_stx + 2: -1]

    # Generate problem info
    prob_info = {}
    prob_info['title'] = title
    prob_info['table'] = prob_table
    prob_info['state'] = ' '.join(state_lines)
    prob_info['input'] = ' '.join(input_lines)
    prob_info['output'] = ' '.join(output_lines)
    prob_info['ex'] = [ '\n'.join(exin_lines), '\n'.join(exout_lines) ]
    return prob_info


def gen_prob_md(info):
    md = '#[' + info['title'] + '](' + info['url'] + ')\n\n'
    md += '| 시간 제한 | 메모리 제한 |\n| :-------: | :---------: |\n'
    md += '| {:<8} | {:<11} |\n\n'.format(info['table'][0], info['table'][1])
    md += '## 문제\n' + wrap_text(info['state']) + '\n'
    md += '## 입력\n' + wrap_text(info['input']) + '\n'
    md += '## 출력\n' + wrap_text(info['output']) + '\n'
    return md


def get_problem(problem):
    url = 'https://acmicpc.net/problem/' + problem
    proc = Popen(['lynx', '-dump', url], stdout=PIPE, stderr=PIPE)
    try:
        outs, errs = proc.communicate()
        lines = outs.decode('utf-8').splitlines()
    except:
        lines = ['Req failed', 'check lynx is executable']

    if not lines[0].strip() in ('Not Found', 'Req failed'):
        prob_info = get_problem_info(lines)
        prob_info['url'] = url
        prob_path = os.environ['BOJ_HOME'] + '/' + problem
        try:
            os.mkdir(prob_path)
            readme = open(prob_path + '/Readme.md', 'w')
            readme.write(gen_prob_md(prob_info))
            readme.close()
            os.mkdir(prob_path + '/testdata')
            in_file = open(prob_path + '/testdata/ex1.in', 'w')
            in_file.write(prob_info['ex'][0])
            in_file.close()
            out_file = open(prob_path + '/testdata/ex1.out', 'w')
            out_file.write(prob_info['ex'][1])
            out_file.close()
        except FileExistsError:
            print('problem ' + problem + ' already exists')
            print('check ' + prob_path)
    else:
        print(lines[0])
        print(lines[1])
