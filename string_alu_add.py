
def string_reverse(string):
    reversed_string = ""
    for i in range(len(string)):
        reversed_string += string[len(string)-1-i]
    return reversed_string

def ALU(op,a,b):
    #ALU
    if(op=="add"):
        return add(a,b)
    if(op=="sub"):
        return sub(a,b)
    if(op=="multiply"):
        return multiply(a,b)
    if(op=="divide"):
        return divide(a,b)
    if(op=="power"):
        return power(a,b)

def add(a,b):
    length_a = len(a)
    length_b = len(b)
    length = 0
    result = ""
    if(length_a>length_b):
        length = length_a
        c = string_reverse(b)
        for i in range(length-length_b):
            c += "0"
        b = string_reverse(c)
    else:
        length = length_b
        if(length>length_a):
            c = string_reverse(a)
            for i in range(length-length_a):
                c += "0"
            a = string_reverse(c)
            
    carry = 0
    index = length-1
    next_carry = 0
    result = ""
    while(index>=0):
        digit_sum = int(a[index])+int(b[index]) + int(next_carry)
        if(digit_sum > 9):
            carry = int(digit_sum / 10)
            digit_sum = digit_sum - 10
        else:
            carry = 0          
        result += str(digit_sum)
        next_carry = carry
        index-=1
    result+= str(next_carry)
    result = string_reverse(result)        
    return result


def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def power(a,b):
    return a**b



#c=["00","09","09","90","00","90"]
#d=["09","00","09","00","90","90"]
    
#for i in range(len(c)):
#    print(ALU("sub",c[i],d[i]))





a=["00","09","09","90","00","90","90909090"*32,"90909090"*32]
b=["09","00","09","00","90","90","99990000","99990000"*32]
for i in range(len(a)):
    print(ALU("add",a[i],b[i]))





























































