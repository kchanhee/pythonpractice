# Define a function that takes a sorted list and the value we want to find,
def binary_search(sorted_list, target):

    # Set the initial search area to be the whole list
    search_area = sorted_list
    if target > sorted_list[-1] or target < sorted_list[0]:
        return print('Not in list!')
    # While the search area has at least 1 element,
    while len(search_area) >= 1:

        # Print the current search area:
        print('Search area:', search_area)

        # Create the index of the last element
        end = len(search_area) - 1

        # Create the index of the first element
        middle = int((0 + end)/2)

        # If target is smaller than the middle value of the search area
        if target < search_area[middle]:
            # Make the new search area the first half of the current search area
            search_area = search_area[:middle]

        # If target is greater than the middle value of the search area
        elif target > search_area[middle]:
            # Make the new search area the second half of the current search area
            search_area = search_area[middle:]

        # If the target is equal to the middle value of the search area:
        else:
            # Print success!
            return print('Found it!', str(search_area[middle]))
    # If the list area has 0 elements, print that search failed
    else:
        return print('Not in list!')

# Run function
sorted_list = list(range(20))

binary_search(sorted_list, 21)
binary_search(sorted_list, -2)
