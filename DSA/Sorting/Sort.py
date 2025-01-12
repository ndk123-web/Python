class sorting:
    def __init__(self):  # Constructor
        pass
    
    def bubble(self, li):  # Bubble Sort: Swap adjacent elements if in wrong order
        for i in range(len(li)):
            for j in range(1, len(li)):
                if li[j-1] > li[j]:
                    li[j-1], li[j] = li[j], li[j-1]
        print('Bubble Sort : ', li)

    def insertion(self, li):  # Insertion Sort: Insert each element into its sorted position
        for i in range(1, len(li)):
            j = i
            while j > 0 and li[j-1] > li[j]:
                li[j-1], li[j] = li[j], li[j-1]
                j -= 1
        print('Insertion Sort : ', li)

    def selection(self, li):  # Selection Sort: Place smallest element at correct position
        for i in range(len(li)):
            min_idx = i
            for j in range(i+1, len(li)):
                if li[min_idx] > li[j]:
                    min_idx = j
            li[min_idx], li[i] = li[i], li[min_idx]
        print('Selection Sort : ', li)

    def merge_sort(self, li):  # Merge Sort: Divide, sort recursively, and merge
        if len(li) <= 1:
            return li
        m = len(li) // 2
        L = self.merge_sort(li[:m])
        R = self.merge_sort(li[m:])
        i = j = k = 0
        while i < len(L) and j < len(R):
            li[k] = L[i] if L[i] < R[j] else R[j]
            i, j = i + (L[i] < R[j]), j + (L[i] >= R[j])
            k += 1
        while i < len(L): li[k], i, k = L[i], i + 1, k + 1
        while j < len(R): li[k], j, k = R[j], j + 1, k + 1
        return li

    def quick_sort(self, li):  # Quick Sort: Divide by pivot and sort recursively
        if len(li) <= 1:
            return li
        pi = li[0]
        L = [x for x in li[1:] if x <= pi]
        R = [x for x in li[1:] if x > pi]
        return self.quick_sort(L) + [pi] + self.quick_sort(R)

    def count_sort(self, li):  # Counting Sort: Count frequencies and build sorted list
        max_val = max(li)
        count_arr = [0] * (max_val +1)
        
        for i in li:
            count_arr[i]+=1
            
        sorted_arr = []
        
        for i in range(len(count_arr)):
            sorted_arr += [i] * count_arr[i]
        
        return sorted_arr
     
        
# Test the sorting methods
li = [1, 5, 4, 2, 3, 11]

bubble = sorting()
bubble.bubble(li)

li = [1, 5, 4, 2, 3, 11]
insert = sorting()
insert.insertion(li)

li = [1, 5, 4, 2, 3, 11]
select = sorting()
select.selection(li)

li = [1, 5, 4, 2, 3, 11]
merge = sorting()
print('Merge Sort : ', merge.merge_sort(li))

li = [1, 5, 4, 2, 3, 11]
quick = sorting()
print('Quick Sort : ', quick.quick_sort(li))

li = [1, 5, 4, 2, 3, 11]
count = sorting()
print('Counting Sort : ', count.count_sort(li))
