'''
Map -> It is used to apply the function to all the elements of the iterable

'''

l = ['1','2','3','4','5']
map_obj = map(lambda x : x+'s',l) # function , itearable obj (list, tuple, etc)
int_list = list(map_obj) 
print(int_list)


'''

filter -> It is used to filter the elements of the iterable based on the condition

'''
    
s = ['1','2','3','4','5']
map_obj = map(int,s)
s =list(map_obj)

filtered = list(filter(lambda x: x>1 ,s))
print(filtered)