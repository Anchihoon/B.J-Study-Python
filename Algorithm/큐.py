#BAEKJOON 10845
import sys
queue = []
n = int(sys.stdin.readline())
for i in range(n):
    w = sys.stdin.readline().split()
    if w[0] == 'push':
        queue.append(int(w[1]))

    elif w[0] == 'pop':
        if queue == [] :
            print('-1')
        else :
            print(queue[0])
            del queue[0]

    elif w[0] == 'size':
        print(len(queue))

    elif w[0] == 'empty':
        if queue == []:
            print('1')
        else :
            print('0')

    elif w[0] == 'front':
        if queue == []:
            print('-1')
        else :
            print(queue[0])

    elif w[0] == 'back':
        if queue == []:
            print('-1')
        else :
            print(queue[len(queue)-1])