def mult(l,r):
    if l < 10 or r < 10:
        return l*r
    
    # Find middle point
    lSize = len(str(l))
    rSize = len(str(r))
    longest = max(lSize, rSize);
    middle = longest/2
    
    # split numbers in the middle
    power = 10**middle
    a = l/power
    b = l%power
    c = r/power
    d = r%power

    # Do Karatsuba magic
    ac = mult(a,c)
    bd = mult(b,d)
    ad_plus_bc = mult(a+b, c+d) - ac - bd
    result = ac*10**(2*middle) + ad_plus_bc*10**middle + bd
    return result

def test(l,r):
    print l
    print r
    print mult(l,r)
    print l*r
    print("\n")

#assert(mult(5,0) == 0)
#assert(mult(5,5) == 25)
#assert(mult(12,34) == 408)
#test(2222,3333)
#test(22222,33333)
#test(222222,333333)
#test(2222222,3333333)
first = 3141592653589793238462643383279502884197169399375105820974944592
second = 2718281828459045235360287471352662497757247093699959574966967627

print mult(first, second)
#print first*second
#assert(mult(123456,75643) == 9338582208)
