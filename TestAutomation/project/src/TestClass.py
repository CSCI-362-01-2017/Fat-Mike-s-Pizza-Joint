# Simple class for testing our system
class TestClass:
    def __init__(self):
        self.value = 0

    def add(self, num):
        self.value += num
        return self.value
