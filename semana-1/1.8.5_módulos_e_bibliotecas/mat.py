def cubo(num):
	return num * num * num 

def fat(num):
	if num <= 1:
		return 1
	return num * fat(num-1)