def mult(l,r):
    print "in mult " + str(l) + " " + str(r)
    if l < 10 or r < 10:
        return long(l)*long(r)
    
    # Find middle point
    lSize = len(str(l))
    rSize = len(str(r))
    longest = max(lSize, rSize);
    middle = longest/2
    
    # TODO Check lecture notes for pseudo code
    # split numbers in the middle
    #lHigh = l/10**middle
    #lLow = l%10**middle
    #rHigh = r/10**middle
    #lLow = r%10**middle

    # Do Karatsuba magic
    #z0 = mult(lLow,rLow)
    #z1 = mult((lLow+lHigh), (rLow+rHigh))
    #z2 = mult(lHigh, rHight)
    #return z2*10**(2*middle) + (z1-z2-z0)*10**(middle) + z0

assert(mult(5,0) == 0)
assert(mult(5,5) == 25)
assert(mult(22,33) == 726)
#assert(mult(123456,75643) == 9338582208)
