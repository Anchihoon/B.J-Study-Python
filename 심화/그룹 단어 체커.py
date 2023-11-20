#BAEKJOON 1316
#set함수는 중복제거하면서 정렬까지 함
cnt = 0

n = int(input())
for i in range(n):
    word = input()
    A = []
    B = []
    j = 0
    while j < len(word) :
        if len(word) == 1:
            break
        else :
            if j == 0:
                A.append(word[j])
                j += 1
            else :
                if word[j] == word[j-1]:
                    j += 1
                else : 
                    A.append(word[j])
                    j += 1
    for k in A:
        if k not in B:
            B.append(k)
    if A == B:
        cnt += 1
print(cnt)