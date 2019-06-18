a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
newStr = ""
if b > a:
    newStr += "b"
    b -= 1
else:
    newStr += "ab"
    c -= 1
flag = False
while a != 0 or b !=0 or c != 0:
    if newStr.endswith("aa" or "bb"):
        flag = True
        break
    else:
        if newStr.endswith("a") and b != 0:
            newStr += "b"
            b -= 1
        elif newStr.endswith("b") and c != 0:
            newStr += "ab"
            c -= 1
        elif newStr.endswith("b") and a != 0:
            newStr += "a"
            a -= 1

if flag is False:
    print(len(newStr))
else:
    print(len(newStr) - 1)
