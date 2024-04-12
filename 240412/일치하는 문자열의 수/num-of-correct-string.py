import sys
n, A = map(str, sys.stdin.readline().split())

count = 0
for _ in range(int(n)):
    target_str = input()
    if target_str == A:
        count += 1

print(count)