Str = input();
newStr = "";
vowels = ['a','e','i','o','u','y','A','I','E','O','U','Y']
for i in Str:
    if(i in vowels):
        continue
    else:
        newStr = newStr + i;
newStr = newStr.lower();
newStr1 = "";
for j in newStr:
    newStr1 = newStr1 + "."  + j;

print(newStr1);
