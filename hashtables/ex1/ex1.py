def get_indices_of_item_weights(weights, length, limit):
    """
    # Merging Two Packages

    Given a package with a weight limit `limit` and a list `weights` of item
    weights, implement a function `get_indices_of_item_weights` that finds
    two items whose sum of weights equals the weight limit `limit`. Your
    function will return a tuple of integers that has the following form:

    ```
    (zero, one)
    ```

    where each element represents the item weights of the two packages.
    _**The higher valued index should be placed in the `zeroth` index and
    the smaller index should be placed in the `first` index.**_ If such a
    pair doesn’t exist for the given inputs, your function should return
    `None`.
    """

    # Instantiate the cache.
    cache = {}
    for i in range(length):
        cache[weights[i]] = i

    # Create (Index, Weight) pairs.
    for i, weight in enumerate(weights):
        # Subtract limit from weight of current object and check if remainder is in hash table (cache).
        remainder = limit - weight
        if remainder in cache:
            i_rem = cache[remainder]
            return (i_rem, i)

    # If no pairs were found to meet the criteria, return none.
    return None
