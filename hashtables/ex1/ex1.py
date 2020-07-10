weights = [4, 6, 10, 15, 16]
length = 5
limit = 21
def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    pair = {}
    for index in range(length):
        # print(index) 0, 1, 2, 3,
        # print(weights) [4, 6, 10, 15, 16]
        # print(weights[index]) 4, 6, 10, 15
        curr_weight = weights[index]
        if curr_weight in pair:
            # print(curr_weight) 15
            prev_index = pair[curr_weight]
            # print(prev_index) 1
            # print(index) 3
            return (index, prev_index)
        pair[limit - weights[index]] = index
        
    return None
        
    

get_indices_of_item_weights(weights, length, limit)

