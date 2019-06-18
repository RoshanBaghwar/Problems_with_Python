n = input()
arrA = list(map(int, input().split()))
d0 = 0
d5 = 0

def Ans(arrA=[], d0, d5):
	ans = ""
	if(d0 == 0):
		ans = -1
	else:
		if(d5 < 9):
			ans = 0
		else:
			q = d5 / 9
			total = int(q) * 9
			ans += "5" * total
			ans += "0" * d0

	return ans

for i in arrA:
		if(i is 0):
			d0 += 1
		else:
			d5 += 1

print(Ans(arrA, int(d0), int(d5)))
