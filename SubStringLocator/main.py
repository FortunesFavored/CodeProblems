str_list = [
    "treebear",
    "treewordbear",
    "trebrow",
    "rewards",
]

import re
from pprint import pprint

# First thing to do is evaluate the first two strings for matching sub strings
potential_substring = list()

pointer = 0

while pointer <= len(str_list[0]):
    sub_pointer1 = pointer + 1
    while sub_pointer1 <= len(str_list[0]):
        potential_match = str_list[0][pointer:sub_pointer1]
        match_status = re.search(potential_match ,str_list[1])
        if match_status:
            potential_substring.append(match_status.group(0))
        sub_pointer1 += 1
    pointer += 1

# The foillowing is all the potential sub strings which may exist
print(potential_substring)

# Now we use the potential list to iterate through the remaining string and determine if any sub-strings actually exist

for i in range(2, len(str_list)):
    pointer = 0
    while pointer < len(potential_substring):
        if re.search(potential_substring[pointer] ,str_list[i]):
            pointer += 1
        else:
            potential_substring.pop(pointer)

# To remove duplicates I make it a set
potential_substring = set(potential_substring)
print(potential_substring)
