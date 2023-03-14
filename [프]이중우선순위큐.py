import heapq

def insert(n, max_pq, min_pq, cnt):
    heapq.heappush(min_pq,n)
    heapq.heappush(max_pq,-n)
    
    if n not in cnt: # 맵에 추가
        cnt[n] = 0
    cnt[n] += 1

def deleteMin(min_pq, cnt):
    if min_pq:
        cnt[min_pq[0]] -= 1 # 개수 줄이기
        if cnt[min_pq[0]] == 0:
            del cnt[min_pq[0]] # 키 삭제?
        
        heapq.heappop(min_pq)
        
def deleteMax(max_pq, cnt):
    if max_pq:
        cnt[-max_pq[0]] -= 1 # 개수 줄이기
        if cnt[-max_pq[0]] == 0:
            del cnt[-max_pq[0]] # 키 삭제?
        
        heapq.heappop(max_pq)

# 반대큐에서 삭제된 값이 top에 남아있지 않도록 정리
def cleanPqs(max_pq, min_pq, cnt):
    while min_pq and min_pq[0] not in cnt:
        heapq.heappop(min_pq)
    while max_pq and -max_pq[0] not in cnt:
        heapq.heappop(max_pq)
    

def solution(operations):
    min_pq = [] # 최소힙
    max_pq = [] # 최대힙
    cnt = {} # 남은 원소의 개수 
    
    for oper in operations:
        cmd = oper[0] # 앞 문자
        n = int(oper[2:]) # 숫자
        
        if cmd == 'I': # 더하기
            insert(n,max_pq,min_pq,cnt)
            print("max:",max_pq,"min:", min_pq)
        else: # 삭제
            if n == 1: # 최대값 삭제
                deleteMax(max_pq, cnt)
            else: # 최소값 삭제
                deleteMin(min_pq, cnt)
                

            cleanPqs(max_pq,min_pq,cnt) # 큐정리
                
    cleanPqs(max_pq,min_pq,cnt) # 큐 정리
    
    if not max_pq or not min_pq:
        return [0,0]
    else:
        return [-max_pq[0], min_pq[0]] #마이너스 왜 붙여??

a = solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])
print(a)
'''

["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]	[0,0]
["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]	[333, -45]
'''