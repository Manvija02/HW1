"""
This contains helper methods for hw2_debugging.py
"""
import subprocess


def random_array(arr):
    """Randomly shuffle the order of an array

    Keyword arguments:
    arr -- Array of integers to be shuffled
    """
    shuffled_num = None
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        arr[i] = int(shuffled_num.stdout)

    return arr
