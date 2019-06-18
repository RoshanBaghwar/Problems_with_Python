
def Fun(ar, i):
	pro = 1
	j = 0
	while(j < len(ar)):
		if(j == i):
			continue
		else:
			pro *= ar[j]
		j += 1
		
	return pro

if __name__ == '__main__':
	ar = [int(x) for x in input().split()]

	for i in range(len(ar)):
		ar[i] = Fun(ar, i)

	print(ar)