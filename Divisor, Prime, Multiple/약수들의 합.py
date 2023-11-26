#BEAKJOON 9506
while True:
    n = int(input())
    if n == -1 :
        break
    A = []
    for i in range(1, n+1):
        if n % i  == 0:
            A.append(i)

    if n != sum(A) - max(A) :
        print(n, 'is NOT perfect.',end='')
    else:
        print(n, '=',end = ' ')
        for i in range(len(A)-1):
            print(A[i],end = ' ')
            if i != len(A) - 2 :
                print('+',end = ' ')
    print()                