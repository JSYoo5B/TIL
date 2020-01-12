#!/usr/bin/env python3
from subprocess import Popen, PIPE
import textwrap


def get_problem_info(lines):
    start = [line for line in lines].index('[21]see all [22][rss.png]')
    end = [line for line in lines].index('노트')
    
    # Check index for problem info
    prob_lines = lines[start + 1:end]
    title_idx = 0
    table_stx = [ln for ln in prob_lines].index('문제 정보')
    state_stx = [ln for ln in prob_lines].index('문제')
    in_stx = [ln for ln in prob_lines].index('입력')
    out_stx = [ln for ln in prob_lines].index('출력')
    ex_in_stx = [ln for ln in prob_lines].index('예제 입력')
    ex_out_stx = [ln for ln in prob_lines].index('예제 출력')
    
    # Extract table data
    table = list(filter(lambda x: x != '*', \
                        prob_lines[table_stx + 1: state_stx]))
    table_lines = [ln[len('+ '):] for ln in table]
    value_stx = [ln for ln in table_lines].index('정답 횟수 (비율)') + 1
    prob_table = table_lines[value_stx + 1: value_stx + 3]

    # Generate problem info
    prob_info = {}
    prob_info['title'] = prob_lines[0]
    prob_info['table'] = prob_table
    prob_info['state'] = ' '.join(prob_lines[state_stx + 1: in_stx])
    prob_info['input'] = ' '.join(prob_lines[in_stx + 1: out_stx])
    prob_info['output'] = ' '.join(prob_lines[out_stx + 1: ex_in_stx])
    prob_info['ex'] = [ '\n'.join(prob_lines[ex_in_stx + 1: ex_out_stx]), \
                        '\n'.join(prob_lines[ex_out_stx+ 1:]) ]
    return prob_info


def gen_prob_md(info):
    md = '#[' + info['title'] + '](' + info['url'] + ')\n\n'
    md += '| 시간 제한 | 메모리 제한 |\n| :-------: | :---------: |\n'
    md += '| {:<9} | {:<11} |\n\n'.format(info['table'][0], info['table'][1])
    md += '## 문제\n' + textwrap.fill(info['state'], 100) + '\n\n'
    md += '## 입력\n' + textwrap.fill(info['input'], 100) + '\n\n'
    md += '## 출력\n' + textwrap.fill(info['output'], 100) + '\n\n'
    return md


def get_problem(problem):
    url = 'https://algospot.com/judge/problem/read/' + problem
    proc = Popen(['lynx', '-dump', url], stdout=PIPE, stderr=PIPE)
    try:
        outs, errs = proc.communicate()
        out_lines = outs.decode('utf-8').splitlines()
        lines = list(filter(None, list(map(lambda x: x.strip(), out_lines))))
    except:
        lines = ['Req failed', 'check lynx is executable']

    if not lines[0] in ('Not Found', 'Req failed'):
        prob_info = get_problem_info(lines)
        prob_info['url'] = url
        print(gen_prob_md(prob_info))
    else:
        print(lines[0])
        print(lines[1])
