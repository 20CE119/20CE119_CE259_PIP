from itertools import combinations

num = [int(n) for n in input().split()]
k = int(input())
cnt = 0
for i in range(1, len(num)+1):
    for c in combinations(num, i):
        if sum(c) == k:
            cnt += 1
print(cnt)
