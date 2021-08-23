#!/usr/bin/env python3

if __name__ == '__main__':
    cnt = int(input())
    sequence = []
    for i in range(cnt):
        num = int(input())
        sequence.append(num)
    
    # Reverse sequence to avoid popleft operation costs
    sequence.reverse()

    operations = ['+']
    current = 2
    stack = [1]
    while len(sequence) > 0:
        top = stack[-1] if len(stack) > 0 else 0
        if sequence[-1] > top:
            stack.append(current)
            current += 1
            operations.append('+')
        elif sequence[-1] == top:
            stack.pop()
            sequence.pop()
            operations.append('-')
        else:
            # Invalid condition, unable to create this sequence
            operations = None
            break

    if operations == None:
        print('NO')
    else:
        print('\n'.join(operations))
