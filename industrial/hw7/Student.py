from Logger import Logger


class Student:
    def __init__(self):
        self.type = 'Student'
        self.logger = Logger()

    def __str__(self):
        return self.type
