# Solution 01
def print_message(value):
    try:
        message = value + " - OK"
        print("No problem, just print the message...")
        print(message)
    except TypeError:
        print("You should know, there was a type error in your program, but I fixed it...")
        message = str(value) + " - OK"
        print(message)


print_message(123)

# Solution 02
try:
    my_list = [1, 2, 0]
    my_list[6] = my_list[1] / my_list[2]
    print(my_list)
except IndexError:
    print("You list's index is out of bound")
except ZeroDivisionError:
    print("You can't divide number by zero")

# output:  You can't divide number by zero