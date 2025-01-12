# 1
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
  
# 2
x = "Navnath"

try:
    if not type(x) is int:
        raise TypeError("Exception")
except:
    print("Numbers Only")