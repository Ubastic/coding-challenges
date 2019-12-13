from functools import reduce


class Automaton:
    def read_commands(self, commands):
        return reduce(lambda state, s: ((0, 1), (2, 1), (1, 1))[state][int(s)], commands, 0) == 1
my_automaton = Automaton()