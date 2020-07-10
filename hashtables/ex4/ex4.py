def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    results = {}
    final_result = []

    for num in a:
        # print(a) [1, -1, 2, 3, -4, -3, 4, -5, 6, 7]
        results[num] = True
        # print(results)
        # print(curr_num) -4, 4, -2, 1, 2, 3, 2, {}
        if -num in results and num != 0:
            # print(-num)
            final_result.append(abs(num))

    return final_result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
