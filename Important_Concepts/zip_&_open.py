'''
zip -> It is used to combine two or more lists into a single list.
'''

names = ['John', 'Doe', 'Jane','ndk']
ages =  [23, 45, 34,19]

for n,a in zip(names,ages):
    print(f'{n} -> {a}')


'''
open -> It is used to open the file in read or write mode
'''

file = open('test.txt','a')
file.write('I am ndk')
file.close()    # It is important to close the file after writing the data

with open('test.txt','r') as file:   # It will close the file automatically
    print(file.read())
    
