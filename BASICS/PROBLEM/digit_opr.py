str = "100/100+(200-100)"

digits = []
oprs = []
prio = ['/','*','+','-']

# SEPARATION
t = ""
for i in str:
    if(i=='+' or i=='-' or i=='*' or i=='/' or i=='(' or i==')'):
        oprs.append(i)
        digits.append(t)
        t=""
    else:
        t = t + i
digits.append(t)
# SEPARATION

# CONVERSION
digits = list(map(float,digits)) 
# CONVERSION

# EVALUATION
def perform(a,b,op):
    match(op):
        case '*':
            return a*b
        case '/':
            return a/b
        case '+':
            return a+b
        case '-':
            return a-b
# EVALUATION

# LOGIC 

def logic(digits,oprs,op1,op2):
    i=0
    while i<len(oprs):
        if oprs[i] in (op1,op2):
            res = perform(digits[i],digits[i+1],oprs[i])
            digits[i]=res
            digits.pop(i+1)
            oprs.pop(i)
        else:
            i+=1

i=0
for i in range(0,len(prio),2):
    op1 = prio[i]
    op2 = prio[i+1] if i+1 < len(prio) else None
    logic(digits,oprs,op1,op2)       
# LOGIC

print(digits , oprs)
