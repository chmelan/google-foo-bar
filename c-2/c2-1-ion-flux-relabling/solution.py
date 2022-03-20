def solution(x,y):
    """Find the id of a bunny worker given a pair of coordinates
    
    Time Complexity:
    O(1)

    Parameters:
        x (int): Distance from vertical wall
        y (int): Height from ground

    Returns:
        id (str): id of bunny
    """


    y_diff = y - 1
    
    # find width of the nearest corner
    x_corner = x + y_diff

    # Calculate the arithmatic sum of the x sequence 
    id = x_corner * (x_corner + 1) / 2

    # Move diagonally to compensate for y 
    id -= y_diff

    return str(id)