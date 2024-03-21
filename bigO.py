# Christopher Blystone
# 3/14/2024
# DRY = Do not Repeat Yourself
# Working on Big O, developing a solution that is more efficient.
# Time complexity (space)
# Big O is a tool to help us compare efficency in turms of time and space in 2 functionaly equivalent pieces of code.
# 1st step=estimating the number of algorithimc steps.
# All of these have 10 algorithmic steps.
# They all visit 10 #'s
# They are all contigous not ordered.
# for i in [1, 10]:
#     print(i)
# for i in range(2, 21, 2):
#     print(i)
# for i in range(10):
#     if is_even(i):
#         print(i)
# Array = fixed size, onece created, the size cannot be changed.
# List = dynamic size, it can grow or shrink.
# Unordered + contiguous Arry
# |  |  |5|10|0|4|-2|20|  |  |  |
# No holse, because the empty spots are at the ends.
# ordered non-contiguous array
# |0|1|2| | |14|24|34| |64|70|100|  |
# This has hole, because they are in the middle and this will give us problems in Big O later on.
a = ("a", "b", "c", "d", "e", "f", )
b = ("1", "2", "3", "4")
mixed = ''
i = 0
j = 0
while i < len(a) or j < len(b):
    if i < len(a):
        mixed += a[i]
        print("mix from a", mixed)
        i += 1
    if j < len(b):
        mixed += b[j]
        print("mix from b", mixed)
        j += 1
print("this is the mixed", mixed)
# if len(a) < len(b):
#     while i < len(b):
#         print(a[i] + b[i])
#         i += 1
# else:
#     while i < len(a):
#         print(a[i] + b[i])
#         i += 1
