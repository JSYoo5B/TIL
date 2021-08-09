#!/usr/bin/env python3

def prefix_traversal(node, tree, traversal):
    left, right = tree[node][0], tree[node][1]
    traversal.append(node)
    if left != '.':
        prefix_traversal(left, tree, traversal)
    if right != '.':
        prefix_traversal(right, tree, traversal)

def infix_traversal(node, tree, traversal):
    left, right = tree[node][0], tree[node][1]
    if left != '.':
        infix_traversal(left, tree, traversal)
    traversal.append(node)
    if right != '.':
        infix_traversal(right, tree, traversal)

def postfix_traversal(node, tree, traversal):
    left, right = tree[node][0], tree[node][1]
    if left != '.':
        postfix_traversal(left, tree, traversal)
    if right != '.':
        postfix_traversal(right, tree, traversal)
    traversal.append(node)


if __name__ == '__main__':
    nodes = int(input())

    tree = {}
    for n in range(nodes):
        node, left, right = input().split()
        tree[node] = [left, right]

    prefix, infix, postfix = [], [], []
    prefix_traversal('A', tree, prefix)
    infix_traversal('A', tree, infix)
    postfix_traversal('A', tree, postfix)

    print(''.join(prefix))
    print(''.join(infix))
    print(''.join(postfix))
