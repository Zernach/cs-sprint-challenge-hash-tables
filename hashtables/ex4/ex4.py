def has_negatives(a):
    """
    # Positive and Negative

    For an input list of integers, we wish to know which positive numbers
    have corresponding negative numbers in the list.

    Example input:

    ```python
    [ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]
    ```

    Input can be in any order.

    Example return value:

    ```python
    [ 1, 3, 4 ]
    ```

    Because 1, 3, and 4 are the positive numbers that have corresponding
    negative numbers in the list.

    Return value can be in any order.

    Solve this problem with a hash table.

    Limits:

    * The input list can contain approximately 5,000,000 elements.
    """
    
    # Instantiate dict for quick referencing.
    ref = {}
    
    # Instantiate a list of nums that have both pos/neg versions in list, a.
    pos_negs = []

    # For every number in the list...
    for num in a:

        # Add that num to the ref dictionary
        ref[num] = num
        
        # If not zero, and if opposite version is in ref, add the abs-value to pos_negs
        if num is not 0 and -num in ref:
            pos_negs.append((abs(num)))

    return pos_negs


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
