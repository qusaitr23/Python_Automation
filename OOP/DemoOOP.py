class Demo:
    def handle_numbers(self, numbers):
        print('The minimum number of the list is: ' + str(self.get_minimum(numbers)))
        print('The maximum number of the list is: ' + str(self.get_maximum(numbers)))
        print('The average number of the list is: ' + str(self.get_average(numbers)))

    def get_minimum(self, numbers):
        minimum = numbers[0]
        for number in numbers:
            if number < minimum:
                minimum = number
        return minimum

    def get_maximum(self, numbers):
        maximum = numbers[0]
        for number in numbers:
            if number > maximum:
                maximum = number
        return maximum

    def get_average(self, numbers):
        sum = 0
        for number in numbers:
            sum += number
        return sum / len(numbers)


list_numbers = [8, 10, 2, 4]
demo1 = Demo()
demo1.handle_numbers(list_numbers)