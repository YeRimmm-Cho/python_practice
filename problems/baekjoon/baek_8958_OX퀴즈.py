TC = int(input())

for _ in range(TC):
    S = input()

    cnt = 0
    result = 0
    i = 0

    while i < len(S):
        
        if S[i] == 'X':
            cnt = 0
            result += cnt
        else:
            cnt += 1
            result += cnt
        
        i += 1
        
    print(result)