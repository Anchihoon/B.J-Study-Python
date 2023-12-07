#BAEKJOON 2231
#for j in range(len(n))
#   sum += n[j] 이런식으로 자릿수합을 했지만 제대로 구해지지않음
n = input()
A = []

for i in range(1,int(n)+1):
    result = i
    digit_sum = sum(map(int, str(i)))
    if result + digit_sum == int(n):
        A.append(i)
        break

if A == []:
    print('0')
else :
    print(A[0])