def main():
	t = int(input())
	while(t > 0):
		t -= 1
		n, a, b = input().split()
		Function(int(n), int(a), int(b))

def Function(n, a, b):
	mid = (a + b) // 2
	if (a < mid and b > mid):
		pos = a + 1
		print(pos, end = " ")
		jump = b - pos + 1
		print(jump)
	else:
		if(a == 1):
			pos = b + 1
			print(pos, end = " ")
			jump = n - pos + 2
			print(jump)
		else:
			pos = a - 1
			print(pos, end = " ")
			jump = n - b + 2
			print(jump)

if __name__ == '__main__':
	main()

