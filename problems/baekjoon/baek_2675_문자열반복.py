T = int(input())    # 테스트 케이스

for tc in range(T):
    R, S = input().split()

    for i in range(len(S)):
        print(int(R) * S[i],end="")
    print()