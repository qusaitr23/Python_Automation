# solution 01
x = 5.5
y = 7.1
if x > y:
    print(x)
elif x < y:
    print(y)
else:
    print("Both are equal")

# solution 02
numbers = [2, 5, 9]
if numbers[0] > numbers[1]:
    print("First one is bigger")
elif numbers[0] < numbers[1]:
    print("Second one is bigger")
else:
    print("Both are equal")

# solution 03 - part a
for num in range(1, 11):
    print(num, end=' ')
print()

# solution 03 - part b
num = 1
while num <= 10:
    print(num, end=' ')
    num += 1
print()

# solution 03 - part c
for num in range(30, 51):
    if num % 2 == 0:
        print(num, end=' ')
print()

# solution 03 - part d
for num in range(20, 41):
    if num % 2 != 0:
        print(num, end=' ')
print()

# solution 04 - part a
countries = ["Austria", "Germany", "Canada", "Peru", "Israel"]
for country in countries:
    print(country, end=' ')
print()

# solution 04 - part b
for country in countries:
    if country == "Israel":
        print("Israel")

# solution 04 - part c
if countries[2] == "China":
    print("Yes, it is there")
else:
    print("No, Sorry...")

# solution 04 - part d
print(len(countries[0]))

# solution 05
age = int(input("Insert your age: "))
if age > 0 and age <= 6:
    print("Go to Kindergarten")
elif age > 6 and age <= 18:
    print("Go to School")
elif age > 18 and age <= 67:
    print("Go to Work")
elif age > 67 and age <= 20:
    print("Collect your pension")

# Other Option
# age = int(input("Insert your age: "))
# if 0 < age <= 6:
#     print("Go to Kindergarten")
# elif 6 < age <= 18:
#     print("Go to School")
# elif 18 < age <= 67:
#     print("Go to Work")
# elif 67 < age <= 20:
#     print("Collect your pension")

# solution 06
profession = input("What is your profession ? ")
if profession.lower() == "teacher":
    salary = 5000
elif profession.lower() == "bank teller":
    salary = 10000
elif profession.lower() == "qa":
    salary = 15000
elif profession.lower() == "average salary":
    salary = 9100
else:
    salary = "Wrong input"

print("Salary is:", salary)

# solution 07
names = {12345: 'qusai', 45678: 'Moshe', 54321: 'David'}
for name in names.keys():
    print("ID:", name)
for name in names.values():
    print("Name:", name)

# solution 08
numbers = {12, 6, 30, 67, 15, 21}
for number in numbers:
    if number % 3 == 0 and number % 5 == 0:
        print(number)


# solution 09
word = ['o', 'l', 'l', 'e', 'h']
while len(word) > 0:
    print(word.pop(), end='')
print()

# solution 10 - part a
numbers = [15, 2, 36, 20, 7]
if numbers[0] > numbers[1]:
    if numbers[0] > numbers[2]:
        print(numbers[0])
    else:
        print(numbers[2])
else:
    if numbers[1] > numbers[2]:
        print(numbers[1])
    else:
        print(numbers[2])

# solution 10 - part b
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print("The maximum value of the list:", max)

# solution 10 - part c
sum = 0
for number in numbers:
    sum += number
print("The sum of elements in the list:", sum)


# solution 11
number = int(input("Enter a number: "))
is_prime = True
for x in range(2, int(number / 2)):
    if number % x == 0:
        is_prime = False
        break
if is_prime:
    print("The number: " + str(number) + " is a prime number")
else:
    print("The number: " + str(number) + " is NOT a prime number")