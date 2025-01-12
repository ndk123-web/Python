import keywords
import platform 
import os 
import sys
import datetime
import math 

# Custom Modules Functions
keywords.func()         
print(keywords.fun1())

# Built In Modules Functions
print(dir(platform))   
print(platform.system())
print(os.name)
print(sys.version)

x = datetime.datetime.now()
print(x.strftime("Today is %A and time is %H:%M:%S")) 

