# from pygorithm.sorting import merge_sort
# print(merge_sort.get_code())
# # print(bubble_sort.get_code())
# list = [2, 3, 4, 8, 12, 22, 2, 8, 5]
# print(merge_sort.sort(list))
'''We have two inputs a and b
we want to get a sume of a and b and out put that to the user.'''


# def solveMeFirst(a, b):
#     return a + b
# def simpleArraySum(ar):
#     num = 0
#     for i in range(len(ar)):
#         num += ar[i]
#         print(i)
#     return num
# Problem 3
"""The task is to find the comparison points by comparing a[0] with b[0] and a[1] and b[1]
If a[1] > b[1] then Alice is awarded 1 point
if a[1] < b[1] then Bob is awarded 1 point
if a[1] = b[1] then neither person receives a point.
Comparison points is the total points a person earned.
Given a and b determine their respective comparison points.
Example:
a = [1,2,3]
b = [3, 2, 1]"""
# Create the function called compareTriplets(a, b):


# def compareTriplets(a, b):
#     # Variable for Alices Comparison score
#     a_comparison = 0
#     # Variable for Bob's Comparison score
#     b_comparison = 0
#     # Create a loop that iterates through both a and b scores
#     for (i, j) in zip(a, b):
#         if i > j:
# # Create the logic that compares a to b and gives a point if either is larger.
#             a_comparison += 1
# # Add the point to variable Alice comparison, or variable Bob's comparison
#         elif i < j:
#             b_comparison += 1
# # Output the Comparison sum with A first and B second.
#     return a_comparison, b_comparison
# Problem 4
'''Complete the aVeryBigSum function which must return the sum of all array elements.
int ar[n]: an array of integers
Return long: the sum of all array elements
Input Format: The first line of the imnput consists of an integer n.
The next line contains n space-separated integers contained in the array.
Output Format: return the integer sum of the elements in the array.'''
# Create the function aVeryBigSum that takes an array.


def aVeryBigSum(ar):
    # Create the variable for the sum of the array.
    sum = 0
    # Create a loop to iterate through the array and add up the integers
    for i in range(len(ar)):
        sum += ar[i]

    return sum


def main():
    # num1 = int(input())
    # num2 = int(input())
    # res = solveMeFirst(num1, num2)
    # print(res)
    # list = [2, 4, 6]
    # print(simpleArraySum(list))
    # alice = [17, 28, 30]
    # bob = [99, 16, 8]
    # print(compareTriplets(alice, bob))

    test = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
    print(aVeryBigSum(test))

    print("end of main")


main()
