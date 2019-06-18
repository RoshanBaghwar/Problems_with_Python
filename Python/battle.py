n,q = input().split()
def Ans(l, r, A=[], B=[]):
	ans = 0;
	for i in range(l-1, r, 1):
		ans += A[i] * B[i]

	return ans

arrA = list(map(int, input().split()))

arrB = list(map(int, input().split()))

for i in range(int(q)):
	l,r = input().split();
	print(Ans(int(l), int(r), arrA, arrB))


