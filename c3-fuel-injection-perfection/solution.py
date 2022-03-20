import time
start_time = time.time()

def solution(n):
    """Return the minimum number of operations required to remove all pellets from que
    
    Arguments:
        n (str): a positive integer input as a string up to 309 characters long


    Returns:
        operations (int): minimum amount of operations  

    Example Output:
        "5: 15 -> 16 -> 8 -> 4 -> 2 -> 1"

    
    """

    #convert n input to long
    pellets = long(n)
    operations = 0

    return operations




def reduce_number(n):
    if n == 1:
        print "minimum number found!"
        print "--- {} seconds ---".format(time.time() - start_time)
        return 

    if n%2 == 0:
        print "dividing {} in half".format(n)
        return reduce_number(n/2)

    # determine if it's better to incriment or decrement
    else:
        print "adding or subtracting 1 from {}".format(n)
        return min(reduce_number(n-1), reduce_number(n+1))
        # print "adding 1 to {}".format(n)
        # reduce_number(n+1)


