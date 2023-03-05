# my code

import sys
input = sys.stdin.readline

N = int(input())

dp = [0 for _ in range(N+1)] # 최소 횟수
path = ["" for _ in range(N+1)] # 최단 경로
path[1] = "1"

for idx in range(2, N+1):
    # 1을 빼는 경우 
    dp[idx] = dp[idx-1] + 1 # 초기화
    prev = idx-1 # 이전 인덱스

    # 3으로 나누는 경우
    if idx % 3 == 0 and dp[idx//3] + 1 < dp[idx]:
        dp[idx] = dp[idx//3] + 1
        prev = idx // 3
    
    # 2로 나누는 경우
    if idx % 2 == 0 and dp[idx//2] + 1 < dp[idx]:
        dp[idx] = dp[idx//3] + 1
        prev = idx // 2

    path[idx] = str(idx) + " " +  path[prev]
    
print(dp[N])
print(path[N])



'''
import sys
input = sys.stdin.readline

N = int(input())

# 1 ~ n 의 각 숫자를 1로 만들기 위해 연산을 하는 횟수의 최솟값 저장 
# 연산 횟수 메모이제이션 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 개수는 N+1
mem = [0]*(N+1) 

# 경로 저장 
# ['', '1', '', '', '', '', '', '', '', '', ''] N+1개
path = ["" for _ in range(N+1)] # 최단 경로
path[1] = "1" # 1은 그냥 1만 저장 

#print(mem)
#print(path)

for idx in range(2, N+1): # 2 ~ 10 
    mem[idx] = mem[idx-1] + 1 # 그 전 횟수에서 1회 추가 
    prev = idx-1 # 이전 인덱스 

    # 3으로 나누어 떨어지고, idx//3+1보다 mem[idx]가 크다 
    if idx % 3 == 0 and mem[idx//3]+1 < mem[idx]:
        mem[idx] = mem[idx//3] + 1 # 연산 횟수 1 추가
        prev = idx // 3 

    # 2으로 나누어 떨어지고, idx//2 + 1 보다 mem[idx]가 크다 
    if idx % 2 == 0 and mem[idx//2]+1 < mem[idx]:
        mem[idx] = mem[idx//2] + 1 # 연산 횟수 1 추가
        prev = idx // 2 

    # 경로 추가 
    path[idx] = str(idx) + " " + path[prev]

print(mem)
print(path)
'''

