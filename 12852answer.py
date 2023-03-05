def calculate(n):
    dp = [[0, 0]] * (n + 1) # [횟수, 쓴 숫자]

    for i in range(2, n + 1):
        #case 3: 1을 뺀다
        dp[i] = [dp[i - 1][0] + 1, i - 1]

		#case 2: X가 2로 나누어 떨어지면, 2로 나눈다
        if (i % 2 == 0 and dp[i // 2][0] < dp[i][0]):
            dp[i] = [dp[i // 2][0] + 1, i // 2]

        #case 1: X가 3으로 나누어 떨어지면, 3으로 나눈다.
        if (i % 3 == 0 and dp[i // 3][0] < dp[i][0]):
            dp[i] = [dp[i // 3][0] + 1, i // 3]

    print(dp)
    '''
    10  
    [[0, 0], [0, 0], [1, 1], [1, 1], [2, 2], [3, 4], [2, 2], [3, 6], [3, 4], [2, 3], [3, 9]]
    '''
    return dp

def solution(n):
    dp = calculate(n)
    result = [0, []] # 횟수와, history 배열
    result[0] = dp[n][0] # 횟수 넣기

    tmp = n #10

    while tmp != 0:
        result[1].append(tmp) # history 넣기
        tmp = dp[tmp][1] # 업뎃

    return result

n = int(input())
result = solution(n)
print(result[0])
print(result[1])