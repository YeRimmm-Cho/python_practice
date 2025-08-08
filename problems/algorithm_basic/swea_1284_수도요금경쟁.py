T = int(input())

for tc in range(1, T+1):
    P,Q,R,S,W = map(int, input().split())

    fare = 0

    A_fare = W * P
    
    if W <= R:
        B_fare = Q
    else:
        B_fare = Q + (W-R) * S

    if A_fare > B_fare:
        fare = B_fare
    else:
        fare = A_fare
    
    print(f"#{tc} {fare}")