# Print
print("Hello World")
print("Hello World", end='')

# String
name = "Yoni"
print(name)
text = "I say: 'Hello' to you"
print(text)
print(text.upper())
print(text.lower())
print(text.count('l'))
print(len(text))
print(text.find('llo'))
print(text.index('llo'))
print(text.replace('world', 'kuku'))
print(text[0])
print(text[-1])
print(text[1:4])
print(text[:2])
print(text[2:])
print(text.split('o'))
str(text)
int(text)

# List
my_list = ['Moshe', 'David', 'Yoni']
print(my_list)
print(my_list[0])
print(my_list[1:2])
print(my_list[:1])
print(my_list[1:])
print(my_list.count('Moshe'))
my_list.insert(3, 'Yael')
my_list.pop(1)
my_list.remove('David')
print(len(my_list))
my_list.reverse()
my_list.sort()

# Set
my_set = {'Moshe', 'David', 'Yoni'}

# Tuple
nums = (1, 2, 3)

# Dictionary
countries = {1: 'Russia', 2: 'Canada', 3: 'Brazil'}
print(countries.get(2))
print(countries.keys())
print(countries.values())
countries[4] = 'USA'

# input
name = input("What is you name? ")

# Operators
a = 5 % 3 # returns 2
result1 = 1 + 2
result2 = 'Hello' +'World'
x = 0
x += 2
x -= 2
x *= 2
x /= 2
x %= 2
y = 0
res1 = x > y
res2 = x > y
res3 = x >= y
res4 = x <= y
res5 = x == y
res6 = x != y
res7 = x > y or x == 1
res8 = x > y and x == 1
print(x in my_list)
print(x not in my_list)

# Statements
aa = 1
if aa == 1:
    pass
else:
    pass

if aa == 1:
    print('1')
elif aa == 2:
    print('2')
else:
    print('3')

if aa > 1:
    if aa < 10:
        print('test')

names = ['aaa', 'bbb', 'ccc']
for name in names:
    print('My Name:', name)

for x in range(5):
    print('test:', x)

for x in range(0, 5):
    print('test:', x)

count = 0
while count < 5:
    print(count)
    count += 1

count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("complete")

count = 0
while count < 5:
    print(count)
    count += 1
    if(count == 2):
        break

count = 0
while count < 5:
    print(count)
    count += 1
    if(count == 2):
        continue


# Functions
def add1():
    print(3 + 4)

def add2():
    return 3 + 4

def add3(a, b):
    print(a + b)

add1()
add2()
add3()

# Errors
try:
    print(10 / 0)
except ZeroDivisionError:
    print('error handled')

# Write - Read Files
def write_file(file_name):
    my_file = open(file_name, "w")
    my_file.write("Test")
    my_file.close()

def read_file(file_name):
    with open(file_name, "r") as my_file:
        data = my_file.read()
        print(data)

write_file('file.txt')
read_file('file.txt')


# OOP
class Car:
    manufacturer = ''
    model = ''
    year = 0
    price = 0.0
    has_abs = False

    def show_details(self):
        print('manufacturer: ' + self.manufacturer + ', model: ' + self.model + ', year: ' + str(
            self.year) + ', price: ' + str(self.price) + ', has ABS ? ' + str(self.has_abs))

    def print_abs(self):
        if self.has_abs:
            print('Car has ABS System')
        else:
            print('Car has No ABS System')


car1 = Car()
car1.manufacturer = 'Toyota'
car1.model = 'Corolla'
car1.year = 2010
car1.price = 19999.99
car1.has_abs = True
car1.show_details()
car1.print_abs()

car2 = Car()
car2.manufacturer = 'Subaru'
car2.model = 'DL'
car2.year = 1981
car2.price = 45.50
car2.has_abs = False
car2.show_details()
car2.print_abs()


class MobileDevice:
    def __init__(self, model, os, version, has_flash, price, screen_width, screen_height):
        self.model = model
        self.os = os
        self.version = version
        self.has_flash = has_flash
        self.price = price
        self.screen_width = screen_width
        self.screen_height = screen_height

    def print_parameters(self):
        print('Model is: ' + self.model + ', Operating System is: ' + self.os + ', Version is: ' + str(self.version) + ', Has Flash ? ' + str(self.has_flash) + ', Price is: ' + str(self.price))

    def calculate_area(self):
        return self.screen_width * self.screen_height

    def picture_quality(self):
        if self.has_flash:
            print('Good Quality')
        else:
            print('Bad Quality')


device1 = MobileDevice('Samsung', 'Android', 8.8, False, 250, 3.5, 6.0)
device1.print_parameters()
print(device1.calculate_area())
device1.picture_quality()

device2 = MobileDevice('Apple', 'IOS', 10.3, True, 3100, 4.0, 7.0)
device2.print_parameters()
print(device2.calculate_area())
device2.picture_quality()