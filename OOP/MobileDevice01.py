class MobileDevice:
    model = ''
    os = ''
    version = 0.0
    has_flash = False
    price = 0

    def print_parameters(self):
        print('Model is: ' + self.model + ', Operating System is: ' + self.os + ', Version is: ' + str(self.version) + ', Has Flash ? ' + str(self.has_flash) + ', Price is: ' + str(self.price))


device1 = MobileDevice()
device1.model = 'Samsung'
device1.os = 'Android'
device1.version = 8.8
device1.has_flash = False
device1.price = 250
device1.print_parameters()

device2 = MobileDevice()
device2.model = 'Apple'
device2.os = 'IOS'
device2.version = 10.3
device2.has_flash = True
device2.price = 3100
device2.print_parameters()

device2 = MobileDevice()
device2.model = 'Apple'
device2.os = 'IOS'
device2.version = 15.3
device2.has_flash = True
device2.price = 5100
device2.print_parameters()