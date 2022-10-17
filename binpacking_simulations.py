def first_fit(list_items, bin_capacity, sort_items=None):
    '''
    Packs items into bins.
    sort_items can be either:
        None (no sorting)
        'increasing' (smallest to largest)
        'decreasing' (largest to smallest)
    '''
    
    # start with one empty bin
    bins = [0]

    # sort the list in decreasing order
    # list_items.sort(reverse=True)

    if sort_items is not None:
        if sort_items == 'increasing':
            # Sort the items smallest to largest
            list_items.sort()
        elif sort_items == 'decreasing':
            # Sort the items largest to smallest
            # list_items.sort(reverse=True)
            list_items[::-1].sort()
        else:
            raise ValueError('Incorrect sort_items!')

    # for loop over the list_items:
    for item in list_items:

        placed = False

        # for loop over the bins:
        for i in range(len(bins)):
            # does it fit?
            # if it fits:
            if item <= bin_capacity - bins[i]:
                # place item in bin
                bins[i] = bins[i] + item
                # raise the flag
                placed = True
                # break the loop
                break

        # if it's not placed in any bins:
        if not placed:
        # if placed == False:
            bins.append(item)
            # # open a new bin
            # bins.append(0)
            # # place the item in new bin
            # bins[-1] = item
    
    # return list of bins
    return bins

# Run some simulations to test the 3 different methods.
N_sets = 1000
N_items = 50
bin_capacity = 40
item_size_limit = [5, 30]

import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt

# Random number generator
rng = default_rng()

# Generate the dataset of all sets of all items
item_sets = rng.integers(item_size_limit[0],
                        item_size_limit[1],
                        endpoint=True,
                        size=(N_sets, N_items))

# print(item_sets)

def total_empty_space(bins, bin_capacity):
    empty_space = 0
    for bin in bins:
        empty_space += bin_capacity - bin
    return empty_space

# Different methods to use
methods = [None, 'increasing', 'decreasing']

fig, ax = plt.subplots(2, 1)

# Try the 3 different methods
for method in methods:
    N_bins = []
    empty_space = []

    for i in range(N_sets):
        # Extract the ith row of the item_sets array
        bins = first_fit(item_sets[i, :], bin_capacity, method)

        # Calculate number of open bins at the end
        N_bins_set = len(bins)
        N_bins.append(N_bins_set)

        # Calculate total empty space in this packing
        empty_space_set = total_empty_space(bins, bin_capacity)
        empty_space.append(empty_space_set)

    # Top plot: scatter plot
    ax[0].plot(range(1, N_sets+1), empty_space, '.', label=f'{method}')

    # Bottom plot: histogram
    ax[1].hist(empty_space, alpha=0.6, label=f'{method}')

ax[0].legend()
ax[0].set(ylabel='Number of open bins')

ax[1].set(xlabel='Number of open bins')
ax[1].legend()
plt.show()
