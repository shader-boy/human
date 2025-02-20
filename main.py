import datetime
from datetime import datetime
import time


class Human:
    def __init__(self, name, age=6, height=106, health=100):
        self.name = name
        self.age = age
        self.height = height
        self.health = health
        self.start_time = datetime.now()

    def grow(self):
        # increases age and height
        pass

    def drink():
        pass

    def eat():
        pass

    def study():
        pass

    def info():
        return f"Name: {self.name}, Age: {self.age}"


new_human = Human("Thomas")
print(new_human.age)
print(new_human.health)

# start_time = datetime.now()

# time.sleep(5)

# end_time = datetime.now()

# elapsed_time = end_time - start_time
# print(elapsed_time)
