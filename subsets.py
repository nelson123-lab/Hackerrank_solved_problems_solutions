def all_subsets(given_array):
    subset = new int[given_array.length()]
    helper(given_array, subset, 0)
def helper(given_array, subset, i):
    if i == given_array.length():
        print_set(subset)
    else:
        subset[i] = null
        helper(given_array, subset, i+1)
        subset[i] = given_array[i]
        helper(given_array, subset, i+1)
p = all_subsets([1,2])
"""
to be corrected
"""
