from Logger import Logger
from Student import Student
from Teacher import Teacher


def main():
    logger = Logger()
    student = Student()
    teacher = Teacher()

    print(logger)
    print(student.logger)
    print(teacher.logger)

    logger.warning('Input may be incorrect')
    student.logger.error('Null pointer exception')


if __name__ == '__main__':
    main()
