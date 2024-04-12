import sys
from collections import deque

n,a,d = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
queue = deque(A)

sequence_list = []
# 우선 첫번째 시작 값부터 찾기
while queue:
    num1 = queue.popleft()
    if num1 != a:
        continue
    else:
        sequence_list.append(num1)
        break

# 첫번째 시작값이 수열 내에 있다면, 그 이후로 등차수열 찾기
if len(sequence_list) != 0:
    while queue:
        num2 = queue.popleft()
        if sequence_list[-1]+d == num2:
            sequence_list.append(num2)
    

print(len(sequence_list))