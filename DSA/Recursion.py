l = []
def fibo(n):
	if n==1 or n==2: return 1
	return fibo(n-1) + fibo(n-2) 

print(fibo(5))

def fact(n):
	if n==1: return 1
	return n*fact(n-1) 
	
print(fact(5))