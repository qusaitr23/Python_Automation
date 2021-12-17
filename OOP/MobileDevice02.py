class MobileDevice:
    model = ''
    os = ''
    version = 0.0
    has_flash = False
    price = 0
    screen_width = 0.0
    screen_height = 0.0

    def print_parameters(self):
        print('Model is: ' + self.model + ', Operating System is: ' + self.os + ', Version is: ' + str(self.version) + ', Has Flash ? ' + str(self.has_flash) + ', Price is: ' + str(self.price))

    def calculate_area(self):
        return self.screen_width * self.screen_height

    def picture_quality(self):
        if self.has_flash:
            print('Good Quality')
        else:
            print('Bad Quality')


device1 = MobileDevice()
device1.model = 'Samsung'
device1.os = 'Android'
device1.version = 8.8
device1.has_flash = False
device1.price = 250
device1.screen_width = 3.5
device1.screen_height = 6.0
device1.print_parameters()
area = device1.calculate_area()
print(area)
device1.picture_quality()

device2 = MobileDevice()
device2.model = 'Apple'
device2.os = 'IOS'
device2.version = 10.3
device2.has_flash = True
device2.price = 3100
device1.screen_width = 4.0
device1.screen_height = 7.0
device2.print_parameters()
area = device1.calculate_area()
print(area)
device2.picture_quality()