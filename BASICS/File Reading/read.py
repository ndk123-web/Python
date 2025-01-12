p = "C:\\Users\\Navnath\\OneDrive\\Desktop\\DeskTop\\Python\\File Reading\\a_test.txt"

with open(p,'r') as f:
    lines = f.readlines();
    print(f.read()) # read and print entire file

for line in lines:
    print(line.strip()) # removes trailing spaces and provide lists
    
with open(p,'w') as w:
    w.write('Hello')    # removes all content and replace with given word
    
with open(p,'a') as r:
    r.write('\nBhai')