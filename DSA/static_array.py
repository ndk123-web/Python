# access elements will be O(1) 
# insertion elements will be O(n)
# deletion elements will be O(n)
# search elements will be O(n)

list = [1,2,3,4,5]

list.insert(0,10)  # On Average O(n)
print('Insert at locatin 0 value',list)

list.append(6)     # On Average O(1)
print("Appending value at end",list)

list.pop()
print("Popping last element of list ",list)

list[0]=11      # On Average O(1)
print("Changing value at index 0", list)

if 3 in list:
    print("Present")
