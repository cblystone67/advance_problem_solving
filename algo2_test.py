'''Problem 1
Complete the diagonalDifference function.
Method takes int arr[n][m]: an array of integers.
Return: int: the absolute diagonal difference
Example:
123
456
989
1+5+9=15
3+5+9=17
|15 - 17| = 2
#Must create a loop that iterates through the three different lists and picks first the [0], [1], [2] then adds up the second [2], [1], [0] then stores those into a variable.  Then find the absolute difference of those two numbers and returns it.'''


def diagonalDifference(arr):
    # Create the vaiables for the multi demensional array
    #

    return 0


def main():
    list = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    row_index = 0
    column_index = 0
    var_right = 0
    var_left = 0
    while row_index < len(list) and column_index < len(list[row_index]):
        var_right += list[row_index][column_index]
        print("varright", var_right)
        row_index += 1
        print("row", row_index)
        column_index += 1
        print("colum", column_index)
        print(var_right)

    row_index = 0
    column_index = 0
    while row_index < len(list) and column_index >= 0:
        var_left += list[row_index][column_index]
        print("varLeft", var_left)
        row_index += 1
        print("row", row_index)
        print("column", column_index)
        column_index -= 1
    print(var_left)
    # total = []
    # sum = 0
    # row_index = 0
    # right = 0
    # left = 0
    # indexer = 2
    # while row_index < len(list):
    #     print("row", row_index)
    #     column_index = 0
    #     while column_index < len(list[row_index]):
    #         print("new Element", list[row_index][column_index])
    #         print("colum", column_index)
    #         if (row_index == indexer-1 and column_index == indexer-1):
    #             right += list[row_index][column_index]
    #             print("right", right)
    #         print("index", indexer)
    #         column_index += 1
    #     row_index += 1
    #     print(right)
    # for row in list:
    #     for element in row:
    #         print("New Element", element)

    # print("The array", total)
    # print("this is the sum", sum)
    # print(diagonalDifference(list))
    print("end of main")


main()
