"""
Creates a random array of integers and uses the merge sort
algorithm to sort the array and print the output.
"""
import rand


def merge_sort(arr):
    """Implementation of merge sort algorithm outputs a sorted array

    Keyword arguments:
    arr -- Array of shuffled integers to be sorted
    """
    if len(arr) == 1:
        return arr

    half = len(arr) // 2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    """Combines to arrays into one array

    Keyword arguments:
    left_arr -- Array to be added on the left
    right_arr -- Array to be added on the right
    """
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            right_index += 1
            merge_arr[left_index + right_index] = left_arr[left_index]
        else:
            left_index += 1
            merge_arr[left_index + right_index] = right_arr[right_index]

    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + right_index] = right_arr[i]

    for i in range(left_index, len(left_arr)):
        merge_arr[left_index + right_index] = left_arr[i]

    return merge_arr


def main():
    """Main body creates an array, sorts it, and prints it
    """
    arr = rand.random_array([None] * 20)
    arr_out = merge_sort(arr)

    print(arr_out)


if __name__ == "__main__":
    main()
