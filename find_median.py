# Author: Clara Hunt
# Github username: huntcl
# Date: 04/29/26
# Description: Returns the median of a list of numbers.

def find_median(num):
    sorted_num = sorted(num)
    length = len(sorted_num)
    middle_index = length // 2

    if length % 2 == 1:
        return sorted_num[middle_index]
    else:
        l_value = sorted_num[middle_index - 1]
        r_value = sorted_num[middle_index]
        return (l_value + r_value) / 2

