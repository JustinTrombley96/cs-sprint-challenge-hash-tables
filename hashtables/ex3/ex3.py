def intersection(arrays):
    """
    YOUR CODE HERE
    """
    results = {}
    final_result = []

    # Your code here
    for array in arrays:
        for num in array:
            if num in results:
                results[num] += 1
                # print(num) 1, 2, 3, 1, 2, 3,
                # print(results[num] 2, 2, 2, 3, 3, 3,
            else:
                results[num] = 1

    for result in results.items():
        if result[1] == len(arrays):
            final_result.append(result[0])
            



    return final_result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
