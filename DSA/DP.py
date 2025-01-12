'''
Top Down Approach:

Time-Complexity: O(n)  -> we are calculating n values after 0,1 
Space-Complexity: O(n) -> we are storing n values in memo

'''
memo={0:0,1:1} # memoization

def top_down_fibo(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = top_down_fibo(n-1)+top_down_fibo(n-2)
        return memo[n]
    
ans = top_down_fibo(6)

print(ans)
print(memo)


'''
Bottom Up Approach:

time-complexity: O(n) -> we are calculating n values after 0,1
space-complexity: O(n) -> we are storing n values in array

'''

ans = 0

def bottom_up_fibo(n):
    arr = [0]*(n+1)
    arr[1]=1
    
    for i in range(2,len(arr)):
        arr[i]=arr[i-1]+arr[i-2] 
    
    return arr[n]

ans = bottom_up_fibo(6)
print(ans)