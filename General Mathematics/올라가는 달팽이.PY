#BAEKJOON 2869
#A=낮에 올라가는 거리, B=밤에 미끄러지는 거리, #V=높이
#하루에 움직이는 거리 A-B
import sys

A, B, V = map(int,sys.stdin.readline().split())

if (V-B) % (A-B) == 0:
    print((V-B) // (A-B))
else:
    print((V-B) // (A-B)+1)