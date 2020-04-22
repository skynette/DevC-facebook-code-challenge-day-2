
# Complete the sockMerchant function below.
#  arr = [1, 2, 1, 2, 1, 3, 2]
#  pair = {'1':1, '2': 1, '3':0}
#  pair.values() = [1,1,0]
#  sum = 1+1 = 2


def sockMerchant(n, arr):
	arr = []
	for i in range(n):
		sock = int(input())
		arr.append(sock)
	pair = {}
	for i in arr:
		occurence = (arr.count(i))//2
		pair[i] = occurence
	
	pair = list(pair.values())
	return sum(pair)



