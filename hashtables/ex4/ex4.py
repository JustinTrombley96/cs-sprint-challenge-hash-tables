a = [1, -1, 2, 3, -4, -3, 4, -5, 6, 7]

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    results = {}
    final_result = []
    for num in a:
        # print(a) [1, -1, 2, 3, -4, -3, 4, -5, 6, 7]
        curr_num = a[num]
        # print(curr_num) -4, 4, -2, 1, 2, 3, 2, {}
        if curr_num < 0:
            # print(curr_num) -4, -2
            results[curr_num] = True
            # print(abs(curr_num)) 4, 2
    for result in results:
        if abs(result) not in a:
            result




    return final_result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
