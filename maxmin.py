"""
Given a list of integers, return the highest and lowest numbers in the array (without using max() or min())
"""

def get_list() -> list[int]:
    # gets list of integers to parse
    list_of_ints = []
    while True:
        new_int = input("Enter an integer, or X to quit: ")
        if new_int == 'X':
            break
        else:
            list_of_ints.append(int(new_int))
    return list_of_ints

def find_min_max(list_of_ints: list[int]) -> list[int]:
    # finds min and max ints in list, outputs [min, max] as list
    highest = list_of_ints[0]
    lowest = list_of_ints[0]

    for num in list_of_ints:
        if num > highest:
            highest = num
        if num < lowest:
            lowest = num

    return [lowest, highest]

print(find_min_max(get_list()))