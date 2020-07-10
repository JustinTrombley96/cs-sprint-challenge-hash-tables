arrays = [
    [1, 2, 3, 4, 5],
    [12, 7, 2, 9, 1],
    [99, 2, 7, 1,]
]
triplets = {}

def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    for array in arrays:
        for num in array:
            if num in triplets:
                triplets[num] += 1
                # print(triplets[num] 2, 2, 2, 3, 3, 3,
            else:
                triplets[num] = 1


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
