def solution(h, q):

    """Finds the parent of each child in a list of nodes in a perfect binary tree(POT) of height h

    Time Complexity:
        O(n log n)
    Parameters:
        h (int): Height of the binary tree
        q (list of int): List of node positions
    
    Returns:
        parent_nodes (list of int): list of parent node positions, if the node doesnt have a parent, return a -1 instead

    """
    
    
    parent_nodes = []

    ## find the max number of nodes in a perfect binary tree of height h
    max_nodes = 2**h - 1

    # loop over nodes and return parent node
    for node in q:

        end_node =  max_nodes
        start_node = 1

        # check if current node is the end node 
        if end_node == node:
            parent_nodes.append(-1)
            continue 

        # loop until the parent node is found
        while (node >= 1):

            end_node = end_node -1

            ## find the midpoint of the tree
            mid_node = start_node + (end_node - start_node)/2

            if (mid_node == node or end_node == node):
                parent_nodes.append(end_node + 1)
                break

            elif(node < mid_node):
                end_node = mid_node
            
            else:
                start_node = mid_node

    return parent_nodes



# def test_solution(h, q, expected):
#     print("RECEIVED:", solution(h, q))
#     assert solution(h, q) == expected, "Should be {}".format(expected)
#     print("Test passed!!")


       


# print("<case 1----------------->")
# test_solution(3, [7, 3, 5, 1], [-1,7,6,3]  )

# print("<case 2----------------->")
# test_solution(5, [19, 14, 28], [21,15,29]  )
