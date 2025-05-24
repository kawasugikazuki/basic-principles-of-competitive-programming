N, S = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

dp = [[False]* (N + 1) for _ in range(S + 1)]

for i in range(S + 1):
  for j in range(N + 1) :
    if i == 0:
      dp[i][j] = True
    else:
      if  i - A[j-1] >= 0 and j > 0  and dp[i - A[j-1]][j - 1]:
        dp[i][j] = True
      if j > 0 and dp[i][j - 1]:
        dp[i][j] = True

print( "Yes" if dp[S][N] else "No")
# print(dp)