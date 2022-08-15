class Robot:
    "class Robot"

    def set_name(self, name):
        self.name = name

    def say_hello(self):
        if hasattr(self, 'name'):
            print(f'Hello, human! My name is {self.name}')
        else:
            print('У робота нет имени')

    def say_bye(self):
        print('See u later alligator')


print(Robot.__doc__)
r2d2 = Robot()
r2d2.set_name('BiBI')
print(r2d2.name)
r2d2.say_hello()

c3po = Robot()
c3po.say_hello()