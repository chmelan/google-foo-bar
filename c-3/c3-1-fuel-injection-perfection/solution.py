def solution(n):
    """Return the minimum number of operations required to reduce a number to 1
    
    Time Complexity:
        O(log n)
        
    Arguments:
        n (str): a positive integer, input as a string up to 309 characters long

    Returns:
        operations (int): minimum number of operations 

    """

    # account for huge numbers
    n = long(n)
    
    operations = 0

    while (n > 1):
        
        # track number of operations
        operations += 1
        
        # if even, divide by 2
        if (n % 2 == 0): 
            n =  n/2 
            continue
        
        # check if subtracting by 1 produces a multiple of 4 
        # or check for the edge case of 3
        # decrement by 1
        elif (n % 4 == 1 or n == 3):
            n -= 1
            continue   

        # otherwise increment by 1
        else:
            n += 1

    return operations