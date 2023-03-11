'''
5(row) 5(col) 
1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
6 5 4 3 2
1 2 1 2 1

5 5
1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
6 5 4 3 2
1 2 1 2 1
'''

import sys; input = sys.stdin.readline

def dfs(x, y, step, total): # total : 합쳐둔 숫자

    global answer

    #파이썬인 경우 시간초과 때문에 백트래킹 사용 => 남은 블럭 개수가 최대값이어도 answer보다 작은 경우 되돌아가
    if total + max_val*(4-step) <= answer:
        return

    if step == 4:
        answer = max(answer, total)
        return

    for dx, dy in d:
        nx = x + dx 
        ny = y + dy 
        # 새로운 좌표가 유효한 범위 내 있고 탐색이력이 없는 경우
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if step == 2 # ㅜ모양 예외 처리
                visited[nx][ny] = True 
                dfs(x, y, step+1, total+board[nx][ny]) # ???
                visited[nx][ny] = False

            visited[nx][ny] = True
            dfs(nx, ny, step+1, total+board[nx][ny])
            visited[nx][ny] = False

if __name__ == "__main__":
    N, M = map(int, input().split()) # 세로(r) 가로 (c)

    board = [list(map(int, input().split())) for _ in range(N)] 

    max_val = max(map(max, board)) # 백트래킹 시 사용

    d = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 좌, 우, 상, 하 

    visited = [[False] * M for _ in range(N)]

    answer = 0

    for i in range(N):
        for j in range(M):
            visited[i][j] = True  # 방문
            dfs(i, j, 1, board[i][j]) # dfs 실행
            visited[i][j] = False # ?? 

    #print(answer)