N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

dp = [float('inf')] * N
dp[0] = 0

for i in range(1,N):
  if i == 1:
    dp[i] = dp[i-1] + A[i-1]
  else:
    dp[i] = min(dp[i-1] + A[i-1], dp[i-2] + B[i-2])

print(dp[N-1])