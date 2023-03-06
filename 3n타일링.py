'''
점화식
dp[n] = dp[n-2] * 3 + dp[n-4] * 2 + dp[n-6] * 2 + ... + dp[2] * 2 + 2 
'''
def solution(n):
    if n%2!=0: # 홀수는 만들 수 있는 경우가 없다. 
        return 0

    dp = [0] * (n + 1) # dp 배열 생성 (0부터니까)
    dp[0] = 1  # 아무것도 두지 않는 경우도 1가지
    dp[2] = 3 

    for i in range(4, n + 1, 2): # 4부터 n까지
        dp[i] = dp[i - 2] * 3

        for j in range(i-4,-1,-2): # i-4부터 0까지
            dp[i]+=dp[j]*2
            
        dp[i]%=1000000007  # 문제에서 나눠주라고 했으니까

    return dp[n]