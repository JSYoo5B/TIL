#!/usr/bin/env python3

import re
from sys import stdin
input = lambda : stdin.readline().rstrip()

if __name__ == '__main__':
    html_doc = input()
    # ignore main tags
    html_doc = html_doc[len('<main>'):-len('</main>')]
    # Change p tags to newline
    html_doc = html_doc.replace('<p>', '')
    html_doc = html_doc.replace('</p>', '\n')
    # Remove div tags (end only)
    html_doc = html_doc.replace('</div>', '')

    # Convert div title
    html_doc = re.sub(r'<div +title="([\w_ ]*)" *>', r"title : \1\n", html_doc)

    # Remove rest tags
    html_doc = re.sub(r'</?[\w_ ]*>', '', html_doc)
    # Reduce blanks into single
    html_doc = re.sub(r' {2,}', ' ', html_doc)
    # Strip end of lines
    html_doc = re.sub(r' ?\n ?', '\n', html_doc)
    html_doc = html_doc.rstrip()

    print(html_doc)
