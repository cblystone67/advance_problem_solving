daysOfWeek = {"Sunday": 1, "Monday": 2, "Tuesaday": 3,
              "Wednesday": 4, "Thursday": 5, "Friday": 6, "Saturday": 7}

print(daysOfWeek.values())
for i in daysOfWeek.keys():
    print(i)
    if i == "Sunday":
        print("Today is Sunday")


# Writing a program that computes the average of a numbers input bny the user, until they enter 0

x = int(input(" > "))
sum = 0
n = 0
while x != 0:
    sum += x
    n += 1
    x = int(input(" > "))

print(sum / n)
