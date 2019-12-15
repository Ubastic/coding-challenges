from threading import Event
from itertools import cycle


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.even_event = Event()
        self.odd_event = Event()
        self.zero_event = Event()
        self.zero_event.set()

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        events = cycle([self.odd_event, self.even_event])
        for _ in range(self.n):
            self.zero_event.wait()
            printNumber(0)
            self.zero_event.clear()
            next(events).set()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.even_event.wait()
            printNumber(i)
            self.even_event.clear()
            self.zero_event.set()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.odd_event.wait()
            printNumber(i)
            self.odd_event.clear()
            self.zero_event.set()