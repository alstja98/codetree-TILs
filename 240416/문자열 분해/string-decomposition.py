from collections import deque

def solution():
    os = input()
    if len(os)%5 != 0:
        return -1
    else:
        n = len(os)//5
        alpha_list = ['a','b','c','d','e']
        alpha_count = []
        for alphabet in alpha_list:
            alpha_count.append(os.count(alphabet))
        
        for count in alpha_count:
            if count != n:
                return -1
        
        if 'abcde'*n == os:
            return 1
        else:
            os = list(os)
            se_list = [[] for _ in range(n)]
            stage = 0
            while set('abcde')&set(os):
                for alphabet in alpha_list:
                    index_num = os.index(alphabet)
                    if alphabet == 'a' or alphabet == 'e':
                        se_list[stage].append(index_num)
                        os[index_num] = '_'
                    else:
                        os[index_num] = '_'

                stage += 1
                
            # print(se_list)
            se_list.sort()
            
            # 최소 그룹 수 계산
            answer = 0
            last_end = -1
            
            for start, end in se_list:
                if start > last_end:
                    # 겹치지 않는 새 그룹
                    answer += 1
                    last_end = end
            if answer == 0:
                return -1
            return answer

if __name__ == '__main__':
    answer = solution()
    print(answer)