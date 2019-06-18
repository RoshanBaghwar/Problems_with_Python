n = int(input())
ar = [int(x) for x in input().split()]

for i in range(n-1):
    a = ar[i]
    b = ar[i+1]
    if (a + b) % 2 == 1:
        if a < b:
            continue
        else:
            ar[i], ar[i+1] = ar[i+1], ar[i]

for i in ar:
    print(i, end=" ")