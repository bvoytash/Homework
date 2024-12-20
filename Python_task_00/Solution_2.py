import numpy as np
import time
from typing import List

def find_elements_in_both_lists(a: List[int], b: List[int]) -> List[int]:
    arr_a = np.array(a)
    arr_b = np.array(b)
    return list(np.intersect1d(arr_a, arr_b))

def find_elements_in_second_list(a: List[int], b: List[int]) -> List[int]:
    arr_a = np.array(a)
    arr_b = np.array(b)
    return list(np.setdiff1d(arr_b, arr_a))

if __name__ == "__main__":
    a = [1, 3, 4, 6, 8, 3, 13]
    b = [2, 4, 5, 6, 4, 12, 8]

    both_list_calculated = find_elements_in_both_lists(a, b)
    only_b_calculated = find_elements_in_second_list(a, b)

    both_lists = set([4, 6, 8])
    only_b = set([2, 5, 12])

    if (
        len(both_list_calculated) == len(both_lists)
        and set(both_list_calculated) == both_lists
    ):
        print(f"Elements in both lists works as expected!")
    else:
        print(f"Elements in both lists is not working")

    if len(only_b_calculated) == len(only_b) and set(only_b_calculated) == only_b:
        print(f"Elements in second list works as expected!")
    else:
        print(f"Elements in second list is not working")


# Both Solution_1 and Solution_2 are qual lines code but if we need less complexity and faster code the second one is much faster.
print("====================")

list_a = np.random.randint(0, 1000000, size=1000000).tolist()
list_b = np.random.randint(0, 1000000, size=1000000).tolist()

# Timing simple Python code
start_time = time.time()
set_a = set(list_a)
set_b = set(list_b)
intersection = list(set_a & set_b)
only_in_b = list(set_b - set_a)
print("Simple Python Code Time:", time.time() - start_time)

# Timing Numpy code
start_time = time.time()
arr_a = np.array(list_a)
arr_b = np.array(list_b)
intersection_np = np.intersect1d(arr_a, arr_b)
only_in_b_np = np.setdiff1d(arr_b, arr_a)
print("Numpy Code Time:", time.time() - start_time)