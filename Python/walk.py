n = int(input());
if(n >= 3):
    arr = list(map(int, input().split()));

def Ans(n, arr):
    last = arr[n-1];
    for i in range(n):
        if(arr[i] is not last):
            dist = n-1 - i;
            if(dist > i):
                max1 = dist;
            else:
                max1 = i;
            break;
    for i in range(n-1, -1, -1):
        first = arr[0];
        if(arr[i] is not first):
            dist = n-1 - i;
            if(dist > i):
                max2 = dist;
            else:
                max2 = i;
            break;
    return max(max1, max2);

print(Ans(n, arr));     
