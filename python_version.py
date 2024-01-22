import math

def o1(n):
    current = 1
    p1 = 1
    p2 = 1
    for i in range (n-2):
        current = p1 + p2
        p1 = p2
        p2 = current
    return current

print(o1(4)) #testcase1 in exam (expected output 3)
print(o1(7)) #testcase2 in exam (expected output 13)
print(o1(100)) #maximum check in exam (expected output 354224848179261915075)

print('--------------------------------------------------------------------------------')
def o2(nMin,nMax):
    return(round((nMax**3-nMin**3)/3+nMax-nMin,3))

print(o2(1,3)) #testcase1 in exam (expected output 10.667)
print(o2(3,10)) #testcase2 in exam (expected output 331.333)

print('--------------------------------------------------------------------------------')
def o3(word):
    word.upper()
    word.split()
    collected = []
    for i in word:
        if i in collected:
            return i+'\n'+ str(word.count(i))
        else:
            collected.append(i)
    return 'NAN' #idk why its all uppercase and string but the exam is like that
        
    

print(o3('TEEAWAT')) #testcase1 in exam (expected output E\n2)
print(o3('COMPUTER')) #testcase3 in exam (expected output NAN)

print('--------------------------------------------------------------------------------')
def o4(a,b,c):
    if b**2-4*a*c < 0:
        return 'NAN'
    else :
        try: return (-b+math.sqrt(b**2-4*a*c))/(2*a)  #<---- the only use of "import math"
        except: return -c/b
print(o4(1,2,6)) #testcase2 in exam (expected output NAN)
print(o4(0,2,1)) #predicted trap in exam (expected output -0.5)