a = int(input());
b = int(input());
c = int(input());
def Ans(a, b ,c):
    base = 0;
    aa = 1;
    bb = 2;
    cc = 4;
    while(a >= aa and b >= bb and c >= cc):
        base += 1;
        aa += 1;
        bb = aa * 2;
        cc = aa * 4;
    
    ans = base + base * 2 + base * 4;
    return ans;

print(Ans(a, b, c));
