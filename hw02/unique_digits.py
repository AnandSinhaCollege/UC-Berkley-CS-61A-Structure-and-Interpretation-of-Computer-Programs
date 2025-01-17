def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    #"*** YOUR CODE HERE ***"
    nnew = list(str(n))
    nnew = [*set(nnew)]
    return len(nnew)
    

def has_digit(n, k):
    """Returns whether K is a digit in N.
    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    #"*** YOUR CODE HERE ***"
    nnew = list(str(n))
    if str(k) in nnew:
        return True
    else:
        return False