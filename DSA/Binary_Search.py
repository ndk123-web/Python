# Traditional Based
def binary(l,r,li,search):
    if l>r:
        return False 
    
    m = (l+r) // 2 
    
    if li[m]==search:
        return True 
    
    if li[m] > search:
        return binary(l,m-1,li,search)
    else:
        return binary(m+1,r,li,search)

li = [1,2,3,4,5,6]
print(binary(0, len(li)-1 , li ,10))

# Condition Based
arr = [True,True,True,True]
def condition_base(arr):
    L = 0
    R = len(arr)-1
    
    while L<R:
        mid = (L+R)//2
        
        if arr[mid]:
            R = mid 
        else:
            L=mid+1
    return L

print(condition_base(arr))