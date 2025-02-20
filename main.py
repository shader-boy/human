import datetime
from datetime import datetime
import time



class Human:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.height = 30
        self.date = datetime.date


    def grow(self):
        # increases age and height
        pass


start_time = datetime.now()

time.sleep(5)

end_time = datetime.now()

elapsed_time = end_time - start_time
print(elapsed_time)
