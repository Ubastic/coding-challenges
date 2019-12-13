from threading import Event

class Foo:
    def __init__(self):
        self.f_event = Event()
        self.s_event = Event()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.f_event.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.f_event.wait()
        printSecond()
        self.s_event.set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.s_event.wait()
        printThird()