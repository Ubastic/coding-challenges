from re import split


class FSM(object):
    def __init__(self, insts: str):
        self.states = {
            k: val for k, *val in
            (map(str.strip, split(r'[;,]', i)) for i in insts.strip().split('\n'))
        }

    def run_fsm(self, start, sequence):
        path = [start]
        for s in sequence:
            path.append(self.states[path[-1]][s])
        return path[-1], int(self.states[path[-1]][-1]), path
