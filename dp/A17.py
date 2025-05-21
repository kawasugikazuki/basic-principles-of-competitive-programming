N = int(input())

A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

dp = [None]* N

dp[0] = 0
dp[1] = A[0]

for i in range(2, N):
  dp[i] = min(dp[i-1] + A[i-1], dp[i-2] + B[i-2])


P = N
ans  = []

while True:
  ans.append(P)
  if P == 1:
    break

  if dp[P - 2] + A[P-2] == dp[P-1]:
    P -= 1
  else:
    P -= 2

print(len(ans))
for i in range(len(ans)-1, -1, -1):
  print(ans[i], end=" ")
print()