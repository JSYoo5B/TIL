#!/usr/bin/env python3
from subprocess import Popen, PIPE
from textformatter import wrap_text
import os


def get_problem_info(lines):
    start = [ln.strip() for ln in lines].index('[21]see all [22][rss.png]')
    end = [ln for ln in lines].index('노트')
    
    # Check index for problem info
    prob_lines = lines[start + 1:end]
    title = prob_lines[1].strip()
    table_stx = [ln for ln in prob_lines].index('문제 정보')
    state_stx = [ln for ln in prob_lines].index('문제')
    in_stx = [ln for ln in prob_lines].index('입력')
    out_stx = [ln for ln in prob_lines].index('출력')
    exin_stx = [ln for ln in prob_lines].index('예제 입력')
    exout_stx = [ln for ln in prob_lines].index('예제 출력')
    
    # Extract table data
    table = list(filter(lambda x: x.strip() != '*', \
                        prob_lines[table_stx + 1: state_stx]))
    table_lines = [ln.strip()[len('+ '):] for ln in table]
    value_stx = [ln for ln in table_lines].index('정답 횟수 (비율)') + 1
    prob_table = table_lines[value_stx + 1: value_stx + 3]
    
    # Extract problem info strings
    del_indent = lambda x: x[len('   '):]
    state_lines = list(map(del_indent, prob_lines[state_stx + 2: in_stx - 1]))
    input_lines = list(map(del_indent, prob_lines[in_stx + 2: out_stx - 1]))
    output_lines = list(map(del_indent, prob_lines[out_stx + 2: exin_stx - 1]))
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
    md += '| {:<9} | {:<11} |\n\n'.format(info['table'][0], info['table'][1])
    md += '## 문제\n' + wrap_text(info['state']) + '\n'
    md += '## 입력\n' + wrap_text(info['input']) + '\n'
    md += '## 출력\n' + wrap_text(info['output']) + '\n'
    return md


def get_problem(problem):
    url = 'https://algospot.com/judge/problem/read/' + problem
    proc = Popen(['lynx', '-dump', url], stdout=PIPE, stderr=PIPE)
    try:
        outs, errs = proc.communicate()
        lines = outs.decode('utf-8').splitlines()
    except:
        lines = ['Req failed', 'check lynx is executable']

    if not lines[0].strip() in ('Not Found', 'Req failed'):
        prob_info = get_problem_info(lines)
        prob_info['url'] = url
        prob_path = os.environ['ALGOSPOT_HOME'] + '/' + problem
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
