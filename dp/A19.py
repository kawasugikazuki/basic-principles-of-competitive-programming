N, W = [int(i) for i in input().split()]

dp = [[0] * (N+1)for _ in range(W+1)]
ws = []
vs = []

for _ in range(N):
  w, v = [int(i) for i in input().split()]
  ws.append(w)
  vs.append(v)

for i in range(W+1):
  for j in range(1, N+1):
    if i - ws[j-1] >= 0:
      dp[i][j] = max(dp[i][j-1], dp[i - ws[j-1]][j-1] + vs[j-1])
    else:
      dp[i][j] = dp[i][j-1]

print(max(dp[W]))