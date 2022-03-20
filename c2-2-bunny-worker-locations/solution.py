def solution(x,y):
    """Find the id of a bunny given a pair of coordinates
    
    Parameters
        x (int): Distance from vertical wall
        y (int): Height from ground

    Returns
        id (str): id of bunny
    
    """


    #
    y_diff = y - 1

    x_end = x + y_diff

    # Calculate the arithmatic sum of the x sequence 
    id = x_end * (x_end + 1) // 2

    # diagonal moves are 
    id -= y_diff

    return str(id)

solution(10,50)     

print(solution(1,4))