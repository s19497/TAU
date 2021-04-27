from src.drivers import *


class MyClass:
    def __init__(self, driver: MyDriver.__class__):
        self.driver = driver

    def helper(self, input_command: str):
        if not len(input_command):
            return
        command, *options = input_command.split(' ')
        driver_options = self.driver.commands.get(command)

        if driver_options is None:
            return

        print([key + ' ' + value for key, value in driver_options.items() if key in options])


the_class = MyClass(LinuxDriver)
the_class.helper('ls -l')
