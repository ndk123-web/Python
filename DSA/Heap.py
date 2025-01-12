# Build Min -Heap 
# Time : O(n) Space : O(1)

A = [-4,3,1,0,2,5,10,8,12,9]

import heapq
heapq.heapify(A)

print(A)

# Heap Push O(log n)
heapq.heappush(A,4)
print(A)

#Heap Pop O(log n)
popped = heapq.heappop(A)
print(A,popped)

#Heap sort O(n log n) space : O(1)
# O(n) + O(n) * O(log n) = O(n log n)

def heapsort(arr):
    heapq.heapify(arr)   # O(n)
    print('Heapify : ',arr)
    new_list = [0] * len(arr)
    
    for i in range(len(arr)):
        minn = heapq.heappop(arr) # O(log n) * O(n) Total = O(n log n)
        new_list[i]=minn
        
    return new_list


    
ans = heapsort([5,6,1,2,0,12,-12,13])
print('Heap Sort : ',ans)