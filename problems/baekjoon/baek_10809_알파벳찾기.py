S = input()     # 문자열 입력
alphabet = 'abcdefghijklmnopqrstuvwxyz'

alpha_lst = [-1] * len(alphabet)

for i in range(len(S)):
    s = S[i]

    for j in range(len(alphabet)):
        if alphabet[j] == s:
            if alpha_lst[j] == -1:   # 처음 위치면
                alpha_lst[j] = i
            break  

print(*alpha_lst)
