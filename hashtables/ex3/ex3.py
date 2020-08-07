def intersection(arrays):

    # Instantiate a list of dictionaries (hash table) to count views-per-digit in each array.
    view_counts = [{}, {}, {}]

    # For each of the arrays, check values, create each value, set equal to 1 (it exists)
    for arr in range(0, len(arrays)):
        for i in arrays[arr]:
            try:
                view_counts[arr][i] = 1
            except:
                pass

    # Got the "large" test to pass, but not the small yet lol
    intersections = []
    # For each number in first dict, check if it's in 2nd and 3rd.
    for num in view_counts[0]:
        if num in view_counts[1] and num in view_counts[2]:
            intersections.append(i)

    print(intersections)
    return intersections


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000,3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000,4000000)) + [1, 2, 3])

    print(intersection(arrays))
