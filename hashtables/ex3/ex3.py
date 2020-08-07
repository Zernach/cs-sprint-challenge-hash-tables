def intersection(arrays):

    # Instantiate a list of dictionaries (hash table) to count views-per-digit in each array.
    view_counts = [{}, {}, {}]

    # For each of the arrays, check values, create each value, set equal to 1 (it exists)
    for arr in range(0, len(arrays)):
        for i in arrays[arr]:
            view_counts[arr][i] = 1

    # Not passing tests yet.
    intersections = []
    for dic in range(0, len(view_counts)):
        for i in view_counts[dic]:
            if i in view_counts[0:2]:
                if i not in intersections:
                    intersections.append(view_counts[dic][i][0])

    return intersections


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000,3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000,4000000)) + [1, 2, 3])

    print(intersection(arrays))
