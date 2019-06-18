A,B = input().split();
x,y,z = input().split();
def Ans(A, B, x, y, z):
	ans = 0;
	yellow = 0;
	blue = 0;
	#for yellow ball
	yellow += x * 2;
	#for green ball
	yellow += y * 1;
	blue += y * 1;
	#for blue ball
	blue += z * 3;

	if(yellow > A):
		ans += yellow - A;
	if(blue > B):
		ans += blue - B;

	return ans;

print(Ans(int(A), int(B), int(x), int(y), int(z)));

