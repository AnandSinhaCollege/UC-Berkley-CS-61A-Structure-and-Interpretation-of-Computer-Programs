def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    flag = False
    for i in range(2,n):
        if n%i==0:
            flag = True
    if flag==False:
        return True
    else:
        return False

