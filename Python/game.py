def main():
	int t = int(input())
	while(t > 0):
		t -= 1
		n = int(input())
		vill = list(int(x) for x in input().split())
		hero = list(int(x) for x in input().split())
		print(Function(n, vill, hero))

def Function(n, vill, hero):
	vill.sort()
	hero.sort()
	count = 0
	ans = "LOSE"
	for i in range(n):
		if(hero[i] > vill[i]):
			count += 1 

	if(count == n):
		ans = "WIN"

	return ans