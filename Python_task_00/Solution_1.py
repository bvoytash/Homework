from typing import List

def find_elements_in_both_lists(a: List[int], b: List[int]) -> List[int]:
    set_a = set(a)
    set_b = set(b)
    return list(set_a & set_b)

def find_elements_in_second_list(a: List[int], b: List[int]) -> List[int]:
    set_a = set(a)
    set_b = set(b)
    return list(set_b - set_a)

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
