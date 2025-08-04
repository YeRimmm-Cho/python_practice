for i in range(1, 11):
    N = int(input())    # 건물 개수
    heights = list(map(int, input().split()))     # N개의 건물 층수

    view_count = 0 
    for j in range(2, N - 2):       # 맨 왼쪽 두 칸과 맨 오른쪽 두 칸에 있는 건물은 항상 높이가 0
        left_heights = max(heights[j-1], heights[j-2])      # j 기준 왼쪽 오른쪽 건물 2개
        right_heights = max(heights[j+1], heights[j+2])
         
        if heights[j] > left_heights and heights[j] > right_heights:
            view_count += heights[j] - max(left_heights, right_heights)
        
    print(f'#{i} {view_count}')