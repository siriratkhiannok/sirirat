def O(n:int):
    if n == 0:
        return
    else:
        return 2*(n-1)+5
    
def D(n:int):
    if n == 0:
        return 1
    else:
        return D(n-1)*n
    
def sumDigit(n:int):
    if n == 0:
        return 0
    else:
        return n%10+sumDigit(n//10)
    
print(sumDigit(45))
print(D(5))
print(O(4))