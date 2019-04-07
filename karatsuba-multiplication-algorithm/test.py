import karatusba as k

def test_mult():
    assert( k.mult(3,4) == 12 )
    assert(k.mult(5,0) == 0)
    assert(k.mult(5,0) == 0)
    assert(k.mult(5,5) == 25)
    assert(k.mult(12,34) == 408)
    assert(k.mult(2222,3333))
    assert(k.mult(22222,33333))
    assert(k.mult(222222,333333))
    assert(k.mult(2222222,3333333))
    assert(k.mult(123456,75643) == 9338582208)

def test_long():
    first = 3141592653589793238462643383279502884197169399375105820974944592
    second = 2718281828459045235360287471352662497757247093699959574966967627
    assert( k.mult(first,second) == first*second) 
