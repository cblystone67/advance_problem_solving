# Christopher Blystone
# March 12, 2024
import pprint


def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def findSubstring(s, k):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    max_vowels = 0
    substring_with_most_vowels = ""
    for i in range(len(s) - k + 1):
        substring = s[i:i+k]
        num_vowels = sum(1 for char in substring if char in vowels)

        if num_vowels > max_vowels:
            max_vowels = num_vowels
            substring_with_most_vowels = substring
    if max_vowels == 0:
        return "Not Found"
    else:
        return substring_with_most_vowels


def main():
    # print(fizzbuzz(20))
    # print(findSubstring('caberqiitefg', 5))

    s = "caberqiitefg"
    k = 5
    # print(findSubstring(s, k))
    vowels = {'a', 'e', 'i', 'o', 'u'}
    max_vowels = 0
    for i in range(len(s) - k + 1):
        substring = s[i:i+k]
        print("Substring", substring)
        num_vowels = 0
        for c in substring:
            if c in vowels:
                num_vowels = num_vowels + 1
        print("num_vow", num_vowels)
        if num_vowels > max_vowels:
            max_vowels = num_vowels
            substring_with_most_vowels = substring
    if max_vowels == 0:
        print("Not Found")
    else:
        print(substring_with_most_vowels)
    pprint.pprint(dir(__builtins__), compact=True)
    print(len(dir(__builtins__)))


main()
