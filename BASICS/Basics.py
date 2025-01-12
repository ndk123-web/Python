import time

# if else
if True:
    print(1)
else:
    print(2)
# if else

#List
li = [1,2,'pa']
print(li)
print(type(li))

for i in li:
    print(i)
    
for i in range (0,len(li)) :
	print(li[i])
 
for i in [0,2]:
    print(li[i])
    
for i in range(3):
    print(li[i])
    
for i,item in enumerate(li):
	print(i,item)
#List

#While

j = len(li)-1
while j>=0:
    print(li[j])
    j-=1

#While

#Functions
z = 10
def our_print(s):
    print(z)
	
our_print("Heloo")
#Functions


# Is function
a = [1,2]
b=[1,2]
c=[1,2]
b=a
print(a is b) # true beacuse a and b are in same location
print(a is c) # false because a and c are in different location
#Is fucntion


#Experiment
x = "Outside"
def check(s):
    x = "inside"
    print(x)    # Ans will be inside

check("")
#Experiment


#Experiment
def add(a,b=5):
    return a+b

print(add(1,2));
#Experiment

#lambda function
x = lambda a,b : a*b
print("Lambda Function",x(1,2)) 
#lambda function