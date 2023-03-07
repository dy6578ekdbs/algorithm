# Union-Find 알고리즘
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 사람 수, 파티 수 
knowList = set(input().split()[1:]) # 아는 사람들 집합
parties = [] #

for _ in range(m): # 파티 수 만큼 반복 
    parties.append(set(input().split()[1:]))


for party in parties:
    if party & knowList: # 교집합이 있다면, 합쳐 
        knowList = knowList.union(party)

cnt = 0

for party in parties:
    if party & knowList: # 교집합 있으면 패스 
        continue
    cnt += 1

print(cnt)

'''

첫째 줄에 사람의 수 N과 파티의 수 M이 주어진다.

둘째 줄에는 이야기의 진실을 아는 사람의 수와 번호가 주어진다. 
진실을 아는 사람의 수가 먼저 주어지고 그 개수만큼 사람들의 번호가 주어진다. 
사람들의 번호는 1부터 N까지의 수로 주어진다.

셋째 줄부터 M개의 줄에는 각 파티마다 오는 사람의 수와 번호가 같은 방식으로 주어진다.

N, M은 50 이하의 자연수이고, 
진실을 아는 사람의 수는 0 이상 50 이하의 정수, 
각 파티마다 오는 사람의 수는 1 이상 50 이하의 정수이다.

4(사람수 N) 3(파티 수 M)
0 (이야기 진실을 아는 사람의 수, 그 사람들의 번호)
2 1 2 (파티마다 오는 사람의 수, 번호)
1 3
3 2 3 4

3 4
1 3
1 1
1 2
2 1 2
3 1 2 3
'''
