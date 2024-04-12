import sys
n = int(input())
num_list = list(map(int, sys.stdin.readline().split()))
answer = 0
for i in range(n,0,-1):
    answer += i*(sorted(num_list)[n-i])

print(answer)