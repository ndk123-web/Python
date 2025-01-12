li=["Apple","banana","Cherry","Kiwi","op"]
print(li[-1])

print(li[0:2]) # except cherry(2)

print(li[-3:-1]) # except op (-1)

li[0:2]=['Banana',"Apple"]  # change list items
print(li)

li.insert(0,"Apple") # insert and shift other elements
print(li)

li.append("orange") #append fruit at the end
print(li)

thistuple = ("F1","F2","F3");   # add tuple and list together
li.extend(thistuple)
print(li)

li.pop(1) # deletes 2nd element (pop)
print(li)

li.pop() # deletes last element (pop)
print(li)

del li[0]   # del keyword can delete list and any value from list
print(li)

li.clear()  # to clear list items
print(li)

li=["Apple","banana","Cherry","Kiwi","op"]
[print(x,end=" , ") for x in li]

print()

# [] we want list where x is variable for x in range(5) means 0 to 4
l = [x for x in range(5)] 
print(l)