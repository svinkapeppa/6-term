from Logger import Logger


class Teacher:
    def __init__(self):
        self.type = 'Teacher'
        self.logger = Logger()

    def __str__(self):
        return self.type
