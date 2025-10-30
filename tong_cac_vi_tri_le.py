n = int(input())
if n == 0:
    print(0)
else:
    a = list(map(int, input().split()))
    result = sum(a[i] for i in range(1, n, 2))
    print(result)