def possible(x,y,n,col):
    for i in range(x): # 놓을 수 있는지 판단
        # 같은 열이나, 대각선에 퀸이 있다면 실패 
        #  col의 차이가 row의 차이와 같다면 대각선으로 겹치는거 
        if y == col[i] or abs(y - col[i]) == x - i: 
            return False
        
    return True

def queen(x,n,col):
    # row가 끝까지 갔다면 (재귀 호출 stop)
    if x == n:
        return 1
    
    count = 0
    
    for y in range(n): # 열 번호 
        if possible(x,y,n,col): # 놓을 수 있다면 
            col[x] = y # 퀸 위치 저장 
            count += queen(x+1, n, col) # 다음 
            
    return count
    
def solution(n):
    
    # [1, 3, 0, 2]라면 [0, 1], [1, 3], [2, 2], [3, 2]에 queen이 배치되어있다.
    # 퀸 위치 중 열 좌표를 저장  
    col = [0] * n 
    
    # 0은 세로축의 시작점 (맨 위 층부터 내려옴)
    # n은 맵의 크기
    # col은 row 의 index를 담기 위한 리스트
    answer = queen(0, n, col)
    
    return answer