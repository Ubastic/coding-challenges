from operator import gt, lt


class Dinglemouse:
    def __init__(self, queues, capacity):
        self.queues = [[*q] for q in queues]
        self.capacity = capacity

    def theLift(self):
        stops = [0]
        lift = []

        people_waiting = True

        def move(queue_with_indexes, comparator):
            nonlocal people_waiting

            for floor, queue in queue_with_indexes:
                if (any(p == floor for p in lift) or any(comparator(p, floor) for p in queue)) and stops[-1] != floor:
                    stops.append(floor)

                lift[:] = [p for p in lift if p != floor]

                for person in queue[:]:
                    if comparator(person, floor):
                        if self.capacity > len(lift):
                            lift.append(person)
                            queue.remove(person)
                        else:
                            people_waiting = True

        while people_waiting:
            people_waiting = False
            move(enumerate(self.queues), gt)
            move(reversed([*enumerate(self.queues)]), lt)

        return [*stops, *([0] if stops[-1] != 0 else [])]