import sys

import numpy as np

import config as cfg


class Encoder:
    def __init__(self, _input, output):
        self.offset = 0
        self.input = _input
        self.output = output
        self.program = np.array([], dtype=np.int32)
        self.static = np.array([], dtype=np.int32)

    @staticmethod
    def get_arguments(word):
        lvl = 0

        for char in word:
            if char == '*':
                lvl += 1
            else:
                arg = word[lvl:]
                try:
                    arg = int(arg)
                except ValueError:
                    arg = cfg.REGISTERS[arg]
                return lvl, arg

    def add(self, words):
        first_lvl, first_arg = self.get_arguments(words[1])
        second_lvl, second_arg = self.get_arguments(words[2])
        return np.array([cfg.COMMAND_ADD, first_lvl, first_arg, second_lvl, second_arg])

    @staticmethod
    def call(words):
        label = hash(words[1])
        return np.array([cfg.COMMAND_CALL, 0, label, 0, 0])

    @staticmethod
    def exit():
        return np.array([cfg.COMMAND_EXIT, 0, 0, 0, 0])

    @staticmethod
    def funcb(words):
        label = hash(words[1])
        return np.array([cfg.COMMAND_FUNCB, 0, label, 0, 0])

    @staticmethod
    def funce():
        return np.array([cfg.COMMAND_FUNCE, 0, 0, 0, 0])

    def goto(self, words):
        first_lvl, first_arg = self.get_arguments(words[1])
        second_lvl, second_arg = self.get_arguments(words[2])
        return np.array([cfg.COMMAND_GOTO, first_lvl, first_arg, second_lvl, second_arg])

    def mov(self, words):
        first_lvl, first_arg = self.get_arguments(words[1])
        second_lvl, second_arg = self.get_arguments(words[2])
        return np.array([cfg.COMMAND_MOV, first_lvl, first_arg, second_lvl, second_arg])

    @staticmethod
    def pop():
        return np.array([cfg.COMMAND_POP, 0, 0, 0, 0])

    def print(self, words):
        first_lvl, first_arg = self.get_arguments(words[1])
        return np.array([cfg.COMMAND_PRINT, first_lvl, first_arg, 0, 0])

    def push(self, words):
        first_lvl, first_arg = self.get_arguments(words[1])
        return np.array([cfg.COMMAND_PUSH, first_lvl, first_arg, 0, 0])

    def putstr(self, line):
        words = line.split(maxsplit=1)[1].strip()
        code = np.array([], dtype=np.int32)
        for char in words:
            code = np.append(code, ord(char))
        self.offset += len(words)
        self.static = np.append(self.static, code)
        return np.array([cfg.COMMAND_PUTSTR, self.offset - len(words), len(words), 0, 0])

    def read(self, words):
        first_lvl, first_arg = self.get_arguments(words[1])
        return np.array([cfg.COMMAND_READ, first_lvl, first_arg, 0, 0])

    def sub(self, words):
        first_lvl, first_arg = self.get_arguments(words[1])
        second_lvl, second_arg = self.get_arguments(words[2])
        return np.array([cfg.COMMAND_SUB, first_lvl, first_arg, second_lvl, second_arg])

    def handle(self, line):
        words = line.split()

        if words[0] == cfg.STR_ADD:
            return self.add(words)
        elif words[0] == cfg.STR_CALL:
            return self.call(words)
        elif words[0] == cfg.STR_EXIT:
            return self.exit()
        elif words[0] == cfg.STR_FUNCB:
            return self.funcb(words)
        elif words[0] == cfg.STR_FUNCE:
            return self.funce()
        elif words[0] == cfg.STR_GOTO:
            return self.goto(words)
        elif words[0] == cfg.STR_MOV:
            return self.mov(words)
        elif words[0] == cfg.STR_POP:
            return self.pop()
        elif words[0] == cfg.STR_PRINT:
            return self.print(words)
        elif words[0] == cfg.STR_PUSH:
            return self.push(words)
        elif words[0] == cfg.STR_PUTSTR:
            return self.putstr(line)
        elif words[0] == cfg.STR_READ:
            return self.read(words)
        elif words[0] == cfg.STR_SUB:
            return self.sub(words)
        else:
            exit('Wrong function')

    def encode(self):
        file = open(self.input, 'r')

        for line in file:
            code = self.handle(line)
            self.program = np.append(self.program, code)

        length = len(self.program) + 1

        self.program = np.array([length, ] + list(self.program) + list(self.static))

        self.program.tofile(self.output)


def main():
    if len(sys.argv) < 3:
        print('Usage: vm.py <input file> <output file>')
    else:
        encoder = Encoder(sys.argv[1], sys.argv[2])

        encoder.encode()


if __name__ == '__main__':
    main()
