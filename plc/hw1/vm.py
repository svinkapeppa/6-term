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

    def next(self):
        self.memory.write(cfg.IP_INDEX, self.ip() + cfg.IP_OFFSET)

    def dereference(self, lvl, value):
        for i in range(lvl):
            value = self.memory.read(value)
        return value

    def add(self, first_lvl, first_arg, second_lvl, second_arg):
        value = self.memory.read(self.dereference(first_lvl, first_arg)) + \
                self.memory.read(self.dereference(second_lvl, second_arg))
        self.memory.write(self.dereference(first_lvl, first_arg), value)

    def mov(self, first_lvl, first_arg, second_lvl, second_arg):
        value = self.memory.read(self.dereference(second_lvl, second_arg))
        self.memory.write(self.dereference(first_lvl, first_arg), value)

    def print(self, first_lvl, first_arg):
        print(self.memory.read(self.dereference(first_lvl, first_arg)))

    def read(self, first_lvl, first_arg):
        value = input()
        self.memory.write(self.dereference(first_lvl, first_arg), value)

    def sub(self, first_lvl, first_arg, second_lvl, second_arg):
        value = self.memory.read(self.dereference(first_lvl, first_arg)) - \
                self.memory.read(self.dereference(second_lvl, second_arg))
        self.memory.write(self.dereference(first_lvl, first_arg), value)

    def handle(self, command, first_lvl, first_arg, second_lvl, second_arg):
        if command == cfg.COMMAND_ADD:
            self.add(first_lvl, first_arg, second_lvl, second_arg)
            self.next()
            return True
        elif command == cfg.COMMAND_CALL:
            return True
        elif command == cfg.COMMAND_EXIT:
            return False
        elif command == cfg.COMMAND_FUNCB:
            return True
        elif command == cfg.COMMAND_FUNCE:
            return True
        elif command == cfg.COMMAND_GOTO:
            return True
        elif command == cfg.COMMAND_MOV:
            self.mov(first_lvl, first_arg, second_lvl, second_arg)
            self.next()
            return True
        elif command == cfg.COMMAND_POP:
            return True
        elif command == cfg.COMMAND_PRINT:
            self.print(first_lvl, first_arg)
            self.next()
            return True
        elif command == cfg.COMMAND_PUSH:
            return True
        elif command == cfg.COMMAND_PUTSTR:
            return True
        elif command == cfg.COMMAND_READ:
            self.read(first_lvl, first_arg)
            self.next()
            return True
        elif command == cfg.COMMAND_SUB:
            self.sub(first_lvl, first_arg, second_lvl, second_arg)
            self.next()
            return True
        else:
            return False

    def _run(self):
        command = self.memory.read(self.ip())
        first_lvl = self.memory.read(self.ip() + 1)
        first_arg = self.memory.read(self.ip() + 2)
        second_lvl = self.memory.read(self.ip() + 3)
        second_arg = self.memory.read(self.ip() + 4)

        return self.handle(command, first_lvl, first_arg, second_lvl, second_arg)

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

        bytecode = np.fromfile(sys.argv[1], dtype=np.int32)

        for i, byte in enumerate(bytecode):
            memory.write(cfg.NUMBER_OF_REGISTERS + i, byte)

        interpreter = Interpreter(memory)
        interpreter.run()

        print(memory.memory)


if __name__ == '__main__':
    main()
