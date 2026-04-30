# Author: Clara Hunt
# Github username: huntcl
# Date: 04/29/26
# Description: Returns a list in its original order after removing duplicates.

def without_duplicates(values):
    unique_values = []

    for value in values:
        print(value)
        if value not in unique_values:
            unique_values.append(value)

    return unique_values

