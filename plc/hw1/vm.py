#!/usr/env/bin python3
import sys

import numpy as np

import config as cfg


class Memory:
    def __init__(self, memory_size):
        self.memory = np.zeros(memory_size, dtype=np.int32)

    def write(self, address, value):
        self.memory[address] = value

    def read(self, address):
        return self.memory[address]


class Interpreter:
    def __init__(self, memory):
        self.memory = memory

    def ip(self):
        return self.memory.read(cfg.IP_INDEX)

    def sp(self):
        return self.memory.read(cfg.SP_INDEX)

    def next(self, offset):
        self.memory.write(cfg.IP_INDEX, self.ip() + offset)

    def handle(self, command, first_arg, second_arg):
        if command == cfg.COMMAND_READ:
            value = input()
            self.memory.write(first_arg, value)
            self.next(3)
            return True
        elif command == cfg.COMMAND_PUTSTR:
            string = chr(second_arg)
            for i in range(3, first_arg + 2):
                string += chr(self.memory.read(self.ip() + i))
            print(string)
            self.next(first_arg + 2)
            return True
        else:
            return False

    def _run(self):
        command = self.memory.read(self.ip())
        first_arg = self.memory.read(self.ip() + 1)
        second_arg = self.memory.read(self.ip() + 2)

        return self.handle(command, first_arg, second_arg)

    def run(self):
        while self._run():
            continue


def main():
    if len(sys.argv) < 2:
        print('Usage: vm.py <file>')
    else:
        memory = Memory(cfg.MEMORY_SIZE)
        memory.write(cfg.IP_INDEX, cfg.NUMBER_OF_REGISTERS)
        memory.write(cfg.SP_INDEX, cfg.MEMORY_SIZE)

        bytecode = np.fromfile(sys.argv[1], dtype=np.int32)[::2]

        for i, byte in enumerate(bytecode):
            memory.write(cfg.NUMBER_OF_REGISTERS + i, byte)

        interpreter = Interpreter(memory)
        interpreter.run()

        print(memory.memory)


if __name__ == '__main__':
    main()
