'''
Sorted -> It is used to sort the elements of the iterable
'''

n = [4,5,-1,6,7,1]
sorted_l = sorted(n,reverse = True ) # It will sort the elements in descending order
print(sorted_l,'\n')

people=[
    {'name':"ndk",'age':20},
    {'name':'ysh','age':21},
    {'name':'shbm','age':19}
]

 # A custom key function can be supplied to customize the sort order, and the
 # reverse flag can be set to request the result in descending order.
sorted_peopel_age = sorted(people,key=lambda person: person['age']) # It will sort the elements based on the age
print(sorted_peopel_age)


'''
Enumerate - returns tuple containing index and value of the elements
'''
l=['a','b','c','d']

for index,chars in enumerate(l):
    print(f'{index+1} -> {chars}')
    
print((enumerate(l))) # It will return the list of tuples containing index and value of the elements