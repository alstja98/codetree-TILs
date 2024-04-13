def make_original(str_num, kind):
    n = len(str_num)
    original = 0
    for i, ele in enumerate(str_num):
        original += int(ele) * (kind ** (n - i - 1))
    return original

def generate_variants(binary_str, base):
    variants = set()
    length = len(binary_str)
    for i in range(length):
        num_list = list(binary_str)
        for j in range(base):
            if num_list[i] != str(j):
                num_list[i] = str(j)
                variants.add(make_original(''.join(num_list), base))
                num_list[i] = binary_str[i]  # 원래 값으로 복구
    return variants

a = input()  # 2진법으로 나타낸 숫자
b = input()  # 3진법으로 나타낸 숫자

# 가능한 N의 변형들 생성
possible_n_from_a = generate_variants(a, 2)
possible_n_from_b = generate_variants(b, 3)

# 두 집합의 교집합 찾기
N = possible_n_from_a.intersection(possible_n_from_b)

# N 출력 (정확히 1개만 존재한다고 가정)
print(N.pop())