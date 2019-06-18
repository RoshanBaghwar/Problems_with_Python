n = int(input())
ar = [int(x) for x in input().split()]
data = ar[0]
flag = True
for i in ar:
    if i != data:
        flag = False
        break

if flag == True:
    print('-1')

else:
    sum1 = 0
    sum2 = 0
    for i in range(n):
        sum1 += ar[i]

    for i in range(n, 2*n):
        sum2 += ar[i]

    if sum1 != sum2:
        for i in ar:
            print(i, end=" ")

    else:
        i = 1
        sum = 0
        arr = []
        while(i < n):
            sum += ar[i] + ar[i + 1] + ar[i + 2]
            if sum != sum1:
                arr = ar[i:] + ar[:i]
            i += 1

        for j in arr:
            print(j, end=" ")



