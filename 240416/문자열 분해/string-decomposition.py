def solution(s):
    n = len(s)
    needed_chars = set('abcde')
    patterns = []

    # abcde의 순서를 유지하며 시작 인덱스를 찾는다
    i = 0
    while i <= n - 5:
        # abcde 순서가 맞는지 확인하면서 인덱스를 추적한다
        found = True
        last_index = i
        next_char_index = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': ''}
        current_char = 'a'
        for j in range(i, n):
            if s[j] == current_char:
                if current_char == 'e':  # 'e'를 찾았다면, 패턴 완성
                    patterns.append((i, j))  # 시작 인덱스와 종료 인덱스 저장
                    i = j  # 다음 탐색을 현재 'e' 이후부터 시작
                    break
                current_char = next_char_index[current_char]
        else:
            break  # 필요한 문자를 찾지 못한 경우 루프 탈출

        i += 1

    if not patterns:
        return -1

    # 겹치지 않는 구간을 계산하여 최소 개수를 찾는다
    patterns.sort()  # 시작 인덱스 기준으로 정렬
    count = 1
    current_end = patterns[0][1]
    for start, end in patterns[1:]:
        if start > current_end:
            count += 1
            current_end = end
        else:
            current_end = max(current_end, end)

    return count

if __name__ == '__main__':
    answer = solution(input())
    print(answer)