T = int(input())

for tc in range(1, T+1):
    N = int(input())
    speed = 0
    time = 0
    
    for i in range(N):
        command = list(map(int, input().split()))
        
        if command[0] == 1:
            speed += command[1]
        elif command[0] == 2:
            speed -= command[1]
            if speed < 0:
                speed = 0
        time += speed
        

    
    print(f"#{tc} {time}")
