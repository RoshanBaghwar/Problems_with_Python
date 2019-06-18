n = int(input())
arr = [int(x) for x in input().split()]

def Fun(arr):
        ans = 0
	if(len(arr) == 2):
		D = abs(arr[0] - arr[1])
		if(D == 0):
			ans = 0
		else:
			for i in range(1, D+1):
				if(arr[0]+i == arr[1]-i):
					ans = i
					break
	return ans


if __name__ == '__main__':
	arr.sort()
	print(Fun(arr))
