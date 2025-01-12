n = [10,20,30,40,50,60]

print(n[1:3])
print(n[-1:])
print(n[:-2])

l = len(n)
print(n[::-1])

# 1

data = [2, 4, 6, 8, 10, 12, 14, 16]
# a) Extract every 2nd element starting from index 1
# b) Extract every 3rd element in reverse order
# c) Extract the sublist [6, 8, 10] using step slicing

print(data[1::2])
print(data[1::3])
print(data[2:5])

# 2
sentence = "SlicingInPythonIsFun"
# a) Extract every alternate character
# b) Extract the substring "Python"
# c) Extract "InPythonIs"

print(sentence[::1])

if "InPython" in sentence:
    print("Exist")
else:
    print("Not Exist")
    
# 3
def is_palindrome(word):
    return word==word[::-1]
    
print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False

# 4
data = [1, 2, 3, 4, 5, 6]
# Replace [2, 3, 4] with ['a', 'b', 'c']

k = 1
chk = [2,3,4]

for i in data:
    if i in chk:
        data[i-1] = chr(k+96)
        k+=1

print(data)

# 5
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output: [[3, 2, 1], [6, 5, 4], [9, 8, 7]]

for i in range(len(matrix)):
    matrix[i] = matrix[i][::-1]
    
print(matrix)

# Matrix 
m = [[1,2,3],[3,4,5],[6,7,8]]

for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j],end=" ")
    print()