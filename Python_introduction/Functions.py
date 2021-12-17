# solution 01
def string_reverse(str1):
    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[index - 1]
        index = index - 1
    print(rstr1)


string_reverse('1234abcd')


# solution 02
def max_of_two(x, y):
    if x > y:
        return x
    return y


def max_of_three(x, y, z):
    return max_of_two(x, max_of_two(y, z))


print(max_of_three(3, 6, -5))


# solution 03
def unique_list(original_list):
    new_list = []
    for element in original_list:
        if element not in new_list:
            new_list.append(element)
    return new_list


print(unique_list([1, 2, 3, 3, 3, 3, 4, 5, 5]))


# solution 04
def print_factorial(num):
    factorial = 1
    if num < 0:
        print("Factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        print("The factorial of", num, "is", factorial)


print_factorial(5)