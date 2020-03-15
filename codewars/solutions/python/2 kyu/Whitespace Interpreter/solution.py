from functools import partial
from inspect import signature
from itertools import count
from typing import Any, Callable, Dict, List, Optional, Tuple

Args = Tuple
Tokens = List[str]
Group = Tuple[str, ...]
Handler = Callable
Handlers = List[Handler]
Labels = Dict[str, int]
Input = List[str]
Output = List[str]
Stack = List[int]
Heap = Dict[str, Any]

SPACE, TAB, LINE_FEED = VALID = ' \t\n'


class ProgramHaltException(Exception):
    pass


class Parser:
    _groups: Dict[Group, Handlers] = {}

    @classmethod
    def register(cls, group_list: Handlers, *tokens: str):
        def decorator(func):
            func.__tokens__ = tokens
            group_list.append(func)
            return func

        return decorator

    @classmethod
    def group(cls, *group: str):
        cls._groups[tuple(group)] = group_list = []

        def decorator(*tokens):
            return cls.register(group_list, *tokens)

        return decorator

    @classmethod
    def _find_group(cls, tokens: Tokens) -> Optional[Tuple[Handlers, Tokens]]:
        for group_tokens, group in cls._groups.items():
            if [*group_tokens] == tokens[:len(group_tokens)]:
                return group, tokens[len(group_tokens):]

    @classmethod
    def _can_handle(cls, handler: Handler, tokens: Tokens, labels: Labels, index: int) -> Optional[Tuple[Args, Tokens]]:
        handler_tokens = handler.__tokens__

        if handler_tokens[-1] in (number, label):
            *handler_tokens, last = handler_tokens

            if [*handler_tokens] == tokens[:len(handler_tokens)]:
                tokens = tokens[len(handler_tokens):]
                value, tokens = last(tokens)

                if handler == mark_with_label:
                    assert value not in labels
                    labels[value] = index

                return (value,), tokens
        elif [*handler_tokens] == tokens[:len(handler_tokens)]:
            return (), tokens[len(handler_tokens):]

    @classmethod
    def _find_handler(cls, tokens: Tokens, labels: Labels, index: int) -> Optional[Tuple[Handler, Tokens]]:
        group, tokens = cls._find_group(tokens)

        for handler in group:
            res = cls._can_handle(handler, tokens, labels, index)

            if res:
                args, tokens = res
                return partial(handler, *args), tokens

    @classmethod
    def parse(cls, tokens: Tokens) -> Tuple[Handlers, Labels]:
        handlers = []
        labels = {}

        for i in count():
            handler, tokens = cls._find_handler(tokens, labels, i)
            handlers.append(handler)

            if not tokens:
                return handlers, labels


def number(tokens: Tokens) -> Tuple[int, Tokens]:
    terminal = tokens.index(LINE_FEED)
    assert terminal

    n = int(''.join(tokens[1:terminal]).replace(SPACE, '0').replace(TAB, '1') or "0", 2)
    return -n if tokens[0] == TAB else n, tokens[terminal + 1:]


def label(tokens: Tokens) -> Tuple[str, Tokens]:
    terminal = tokens.index(LINE_FEED) + 1
    l, tokens = tokens[:terminal], tokens[terminal:]

    return ''.join(l), tokens


stack_group = Parser.group(SPACE)


@stack_group(SPACE, number)
def push_to_stack(n: int, stack: Stack):
    stack.append(n)


@stack_group(TAB, SPACE, number)
def duplicate_the_nth_value_from_stack_top(n: int, stack: Stack):
    assert 0 <= n < len(stack)
    stack.append(stack[-(n + 1)])


@stack_group(TAB, LINE_FEED, number)
def discard_top_n_values(n, stack):
    if n < 0 or n > len(stack):
        del stack[:-1]
    else:
        del stack[-(n + 1): -1]


@stack_group(LINE_FEED, SPACE)
def duplicate_top_value(stack):
    stack.append(stack[-1])


@stack_group(LINE_FEED, TAB)
def swap_top_values(stack: Stack):
    stack[-1], stack[-2] = stack[-2], stack[-1]


@stack_group(LINE_FEED, LINE_FEED)
def discard_top_value(stack: Stack):
    stack.pop()


arithmetic_group = Parser.group(TAB, SPACE)


@arithmetic_group(SPACE, SPACE)
def arithmetic_add(stack: Stack):
    a, b = stack.pop(), stack.pop()
    stack.append(b + a)


@arithmetic_group(SPACE, TAB)
def arithmetic_sub(stack):
    a, b = stack.pop(), stack.pop()
    stack.append(b - a)


@arithmetic_group(SPACE, LINE_FEED)
def arithmetic_mul(stack):
    a, b = stack.pop(), stack.pop()
    stack.append(b * a)


@arithmetic_group(TAB, SPACE)
def arithmetic_div(stack):
    a, b = stack.pop(), stack.pop()
    stack.append(b // a)


@arithmetic_group(TAB, TAB)
def arithmetic_mod(stack):
    a, b = stack.pop(), stack.pop()
    stack.append(b % a)


heap_group = Parser.group(TAB, TAB)


@heap_group(SPACE)
def heap_store(stack, heap):
    a, b = stack.pop(), stack.pop()
    heap[b] = a


@heap_group(TAB)
def heap_push(stack, heap):
    stack.append(heap[stack.pop()])


input_output_group = Parser.group(TAB, LINE_FEED)


@input_output_group(SPACE, SPACE)
def output_character(stack: Stack, output: Output):
    output.append(chr(stack.pop()))


@input_output_group(SPACE, TAB)
def output_number(stack, output):
    output.append(str(int(stack.pop())))


@input_output_group(TAB, SPACE)
def read_character(stack: Stack, heap: Heap, input: Input):
    a, b = input.pop(0), stack.pop()
    heap[b] = ord(a)


@input_output_group(TAB, TAB)
def read_number(stack: Stack, heap: Heap, input: Input):
    assert stack
    b = stack.pop()

    while True:
        a = input.pop(0)

        if a.isdigit():
            heap[b] = int(a)
            break


flow_group = Parser.group(LINE_FEED)


@flow_group(SPACE, SPACE, label)
def mark_with_label(_: str):
    pass


@flow_group(SPACE, TAB, label)
def call_subroutine(l: str, labels: Labels, ip: int, call_stack: Stack) -> int:
    call_stack.append(ip + 1)
    return jump_force(l, labels)


@flow_group(SPACE, LINE_FEED, label)
def jump_force(l: str, labels: Labels) -> int:
    return labels[l]


@flow_group(TAB, SPACE, label)
def jump_on_zero(l: str, stack: Stack, labels: Labels) -> int:
    if stack.pop() == 0:
        return jump_force(l, labels)


@flow_group(TAB, TAB, label)
def jum_when_less(l: str, stack: Stack, labels: Labels) -> int:
    if stack.pop() < 0:
        return jump_force(l, labels)


@flow_group(TAB, LINE_FEED)
def exit_subroutine(call_stack) -> int:
    return call_stack.pop()


@flow_group(LINE_FEED, LINE_FEED)
def exit_program():
    raise ProgramHaltException


def _get_additional_kwargs(func: partial, kwargs: Dict[str, Any]) -> Dict[str, Any]:
    additional = {p for p in [*signature(func.func).parameters.keys()][len(func.args):]}
    return {key: kwargs[key] for key in kwargs.keys() & additional}


def run(handlers: Handlers, labels: Labels, input: Input) -> Output:
    context = {
        'input': input,
        'output': [],
        'stack': [],
        'heap': {},
        'labels': labels,
        'call_stack': [],
        'ip': 0,
    }

    ip = 0
    try:
        while True:
            context['ip'] = ip

            handler = handlers[ip]
            new_ip: Optional[int] = handler(**_get_additional_kwargs(handler, context))

            ip = new_ip if new_ip is not None else ip + 1
    except ProgramHaltException:
        pass

    return context['output']


def whitespace(code: str, inp: str = '') -> str:
    return ''.join(run(*Parser.parse([c for c in code if c in VALID]), [*inp]))