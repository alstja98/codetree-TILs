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
            answer = 1
            os = list(os)
            while os:
                is_end = False
                for alphabet in alpha_list:
                    os_str = os[0]
                    if is_end == True:
                        os.remove(alphabet)
                    else:
                        if os_str == alphabet:
                            os.remove(alphabet)
                        else:
                            answer += 1
                            is_end = True
                            os.remove(alphabet)

            return answer

if __name__ == '__main__':
    answer = solution()
    print(answer)