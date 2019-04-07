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

