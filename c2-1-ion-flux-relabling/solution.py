def solution(h, q):

    """Finds the parent of each child node in a list of nodes that belong to a perfect binary tree

    Time Complexity:
        O(n log n)
        
    Parameters:
        h (int): Height of the binary tree
        q (list of int): List of node positions
    
    Returns:
        parent_nodes (list of int): List of parent node positions, root nodes return -1
    """
    
    
    parent_nodes = []

    # find the max number of nodes in a perfect binary tree of height h
    max_nodes = 2**h - 1

    # loop over node list and return parent node
    for node in q:

        end_node =  max_nodes
        start_node = 1

        # check if current node is the end node 
        if end_node == node:
            parent_nodes.append(-1)
            continue 

        # loop over tree until the parent node is found
        while (node >= 1):

            end_node = end_node -1

            #find the midpoint of the tree
            mid_node = start_node + (end_node - start_node)/2
            
            #if the node has been found, add it to the parent_nodes list and end the loop 
            if (mid_node == node or end_node == node):
                parent_nodes.append(end_node + 1)
                break
            
            # if the node is less than the mid_node search the left subtree 
            elif(node < mid_node):
                end_node = mid_node
                
            # otherwise, search the the right subtree 
            else:
                start_node = mid_node

    return parent_nodes
