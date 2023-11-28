#BAEKJOON 1085
import sys

x, y, w, h = map(int,sys.stdin.readline().split())
W = w - x
H = h - y
A = [W, H, x, y]
print(min(A))