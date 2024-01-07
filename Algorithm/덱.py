#BAEKJOON 10866
import sys

n = int(sys.stdin.readline())
deque = []
for i in range(n):
    w = sys.stdin.readline().split()
    if w[0] == 'push_front':
        deque.insert(0, int(w[1]))

    elif w[0] == 'push_back':
        deque.append(int(w[1]))

    elif w[0] == 'pop_front':
        if deque == []:
            print('-1')
        else :
            print(deque[0])
            del deque[0]

    elif w[0] == 'pop_back':
        if deque == []:
            print('-1')
        else :
            print(deque[len(deque) - 1])
            del deque[len(deque) - 1]

    elif w[0] == 'size':
        print(len(deque))

    elif w[0] == 'empty':
        if deque == []:
            print('1')
        else :
            print('0')

    elif w[0] == 'front':
        if deque == []:
            print('-1')
        else:
            print(deque[0])

    elif w[0] == 'back':
        if deque == []:
            print('-1')
        else :
            print(deque[len(deque) - 1])