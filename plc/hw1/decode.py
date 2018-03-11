import sys

import numpy as np

import config as cfg


class Decoder:
    def __init__(self, _input, output):
        self.offset = 0
        self.input = _input
        self.output = output
        self.program = np.array([], dtype=np.int32)
        self.static = np.array([], dtype=np.int32)

    @staticmethod
    def get_argument(lvl, arg):
        if lvl == 0:
            return ' ' + str(arg)
        else:
            return ' ' + '*' * lvl + cfg.REGISTERS_REVERSE[arg]

    def add(self, first_lvl, first_arg, second_lvl, second_arg):
        string = cfg.STR_ADD + self.get_argument(first_lvl, first_arg) + \
                 self.get_argument(second_lvl, second_arg) + '\n'
        return string

    @staticmethod
    def call(first_arg):
        string = cfg.STR_CALL + ' ' + str(first_arg) + '\n'
        return string

    @staticmethod
    def exit():
        string = cfg.STR_EXIT + '\n'
        return string

    @staticmethod
    def funcb(first_arg):
        string = cfg.STR_FUNCB + ' ' + str(first_arg) + '\n'
        return string

    @staticmethod
    def funce():
        string = cfg.STR_FUNCE + '\n'
        return string

    @staticmethod
    def goto(first_lvl, first_arg, second_arg):
        string = cfg.STR_GOTO + ' ' + '*' * first_lvl + cfg.REGISTERS_REVERSE[first_arg] + \
                 ' ' + str(second_arg) + '\n'
        return string

    def mov(self, first_lvl, first_arg, second_lvl, second_arg):
        string = cfg.STR_MOV + self.get_argument(first_lvl, first_arg) + \
                 self.get_argument(second_lvl, second_arg) + '\n'
        return string

    @staticmethod
    def pop():
        string = cfg.STR_POP + '\n'
        return string

    def print(self, first_lvl, first_arg):
        string = cfg.STR_PRINT + self.get_argument(first_lvl, first_arg) + '\n'
        return string

    def push(self, first_lvl, first_arg):
        string = cfg.STR_PUSH + self.get_argument(first_lvl, first_arg) + '\n'
        return string

    def putstr(self, data, first_lvl, first_arg):
        string = cfg.STR_PUTSTR + ' '
        for i in range(first_arg):
            string += chr(data[self.offset + first_lvl + i])
        string += '\n'
        return string

    def read(self, first_lvl, first_arg):
        string = cfg.STR_READ + self.get_argument(first_lvl, first_arg) + '\n'
        return string

    def sub(self, first_lvl, first_arg, second_lvl, second_arg):
        string = cfg.STR_SUB + self.get_argument(first_lvl, first_arg) + \
                 self.get_argument(second_lvl, second_arg) + '\n'
        return string

    def handle(self, data, command, first_lvl, first_arg, second_lvl, second_arg):
        if command == cfg.COMMAND_ADD:
            return self.add(first_lvl, first_arg, second_lvl, second_arg)
        elif command == cfg.COMMAND_CALL:
            return self.call(first_arg)
        elif command == cfg.COMMAND_EXIT:
            return self.exit()
        elif command == cfg.COMMAND_FUNCB:
            return self.funcb(first_arg)
        elif command == cfg.COMMAND_FUNCE:
            return self.funce()
        elif command == cfg.COMMAND_GOTO:
            return self.goto(first_lvl, first_arg, second_arg)
        elif command == cfg.COMMAND_MOV:
            return self.mov(first_lvl, first_arg, second_lvl, second_arg)
        elif command == cfg.COMMAND_POP:
            return self.pop()
        elif command == cfg.COMMAND_PRINT:
            return self.print(first_lvl, first_arg)
        elif command == cfg.COMMAND_PUSH:
            return self.push(first_lvl, first_arg)
        elif command == cfg.COMMAND_PUTSTR:
            return self.putstr(data, first_lvl, first_arg)
        elif command == cfg.COMMAND_READ:
            return self.read(first_lvl, first_arg)
        elif command == cfg.COMMAND_SUB:
            return self.sub(first_lvl, first_arg, second_lvl, second_arg)
        else:
            exit('Wrong function')

    def decode(self):
        data = np.fromfile(self.input, dtype=np.int32)[::2]

        output = open(self.output, 'w')

        self.offset = data[0]
        limit = int((self.offset - 1) / cfg.IP_OFFSET)

        for i in range(limit):
            command = data[cfg.IP_OFFSET * i + 1]
            first_lvl = data[cfg.IP_OFFSET * i + 2]
            first_arg = data[cfg.IP_OFFSET * i + 3]
            second_lvl = data[cfg.IP_OFFSET * i + 4]
            second_arg = data[cfg.IP_OFFSET * i + 5]

            string = self.handle(data, command, first_lvl,
                                 first_arg, second_lvl, second_arg)

            output.write(string)


def main():
    if len(sys.argv) < 3:
        print('Usage: vm.py <input file> <output file>')
    else:
        decoder = Decoder(sys.argv[1], sys.argv[2])

        decoder.decode()


if __name__ == '__main__':
    main()
