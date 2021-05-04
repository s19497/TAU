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

        return ', '.join([key + ' ' + value for key, value in driver_options.items() if key in options])

    @staticmethod
    def fib(n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a
