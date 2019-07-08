from typing import NamedTuple, Sequence

SUITS = ["S", "H", "D", "C"]
CARD_VALUE = "23456789TJQKA"

WIN = "Win"
LOSS = "Loss"
TIE = "Tie"

RESULT = [WIN, LOSS, TIE]


class Card(NamedTuple):
    value: str
    suite: str


class Combination:
    rank = 0

    def __init__(self, cards: Sequence[Card]):
        self.cards = cards

    def __repr__(self):
        return f"{type(self).__name__}(cards={self.cards!r})"

    @staticmethod
    def cards_check(cards1, cards2):
        m1 = sorted((c.value for c in cards1), key=CARD_VALUE.index, reverse=True)
        m2 = sorted((c.value for c in cards2), key=CARD_VALUE.index, reverse=True)

        for mm1, mm2 in zip(m1, m2):
            res = Combination.compare_values(mm1, mm2)
            if res != TIE:
                return res

        return TIE

    def compare(self, other: 'Combination'):
        if other.rank == self.rank:
            res = self.same_rank_compare(other)

            if res == TIE:
                return self.cards_check(self.cards, other.cards)
            else:
                return res
        elif other.rank < self.rank:
            return WIN
        else:
            return LOSS

    def same_rank_compare(self, other: 'Combination'):
        raise NotImplemented

    @classmethod
    def compare_values(cls, m1, m2):
        if m1 == m2:
            return TIE
        elif CARD_VALUE.index(m1) < CARD_VALUE.index(m2):
            return LOSS
        else:
            return WIN

    @classmethod
    def create(cls, cards: Sequence[Card]):
        raise NotImplemented


class HighCard(Combination):
    rank = 1

    def same_rank_compare(self, other: 'Combination'):
        return TIE

    @classmethod
    def create(cls, cards: Sequence[Card]):
        return cls(cards)


class Pair(Combination):
    rank = 2

    @staticmethod
    def get_pairs(cards: Sequence[Card], count=2):
        values = [c.value for c in cards]
        return [v for v in set(values) if values.count(v) == count]

    def same_rank_compare(self, other: 'Combination'):
        m1 = max(Pair.get_pairs(self.cards))
        m2 = max(Pair.get_pairs(other.cards))

        return self.compare_values(m1, m2)

    @classmethod
    def create(cls, cards: Sequence[Card]):
        if Pair.get_pairs(cards):
            return cls(cards)


class TwoPairs(Combination):
    rank = 3

    def same_rank_compare(self, other: 'Combination'):
        m1 = max(Pair.get_pairs(self.cards))
        m2 = max(Pair.get_pairs(other.cards))

        return self.compare_values(m1, m2)

    @classmethod
    def create(cls, cards: Sequence[Card]):
        values = [c.value for c in cards]
        if [values.count(v) for v in set(values)].count(2) == 2:
            return cls(cards)


class ThreeOfAKind(Combination):
    rank = 4

    def same_rank_compare(self, other: 'Combination'):
        m1 = max(Pair.get_pairs(self.cards, count=3))
        m2 = max(Pair.get_pairs(other.cards, count=3))

        return self.compare_values(m1, m2)

    @classmethod
    def create(cls, cards: Sequence[Card]):
        values = [c.value for c in cards]
        if any(values.count(v) == 3 for v in set(values)):
            return cls(cards)


class Straight(Combination):
    rank = 5

    def same_rank_compare(self, other: 'Combination'):
        m1 = min(c.value for c in self.cards)
        m2 = min(c.value for c in other.cards)

        return self.compare_values(m1, m2)

    @classmethod
    def create(cls, cards: Sequence[Card]):
        if "".join(sorted((c.value for c in cards), key=CARD_VALUE.index)) in CARD_VALUE + CARD_VALUE:
            return cls(cards)


class Flush(Combination):
    rank = 6

    def same_rank_compare(self, other: 'Combination'):
        m1 = min(c.value for c in self.cards)
        m2 = min(c.value for c in other.cards)

        return self.compare_values(m1, m2)

    @classmethod
    def create(cls, cards: Sequence[Card]):
        if len(set(c.suite for c in cards)) == 1:
            return cls(cards)


class FullHouse(Combination):
    rank = 7

    def same_rank_compare(self, other: 'Combination'):
        m1 = max(Pair.get_pairs(self.cards, count=3))
        m2 = max(Pair.get_pairs(other.cards, count=3))

        return self.compare_values(m1, m2)

    @classmethod
    def create(cls, cards: Sequence[Card]):
        values = [c.value for c in cards]
        if len(set(values)) == 2 and max(values.count(v) for v in values) == 3:
            return cls(cards)


class FourOfAKind(Combination):
    rank = 8

    def same_rank_compare(self, other: 'Combination'):
        m1 = max(Pair.get_pairs(self.cards, count=4))
        m2 = max(Pair.get_pairs(other.cards, count=4))

        return self.compare_values(m1, m2)

    @classmethod
    def create(cls, cards: Sequence[Card]):
        values = [c.value for c in cards]
        if any(values.count(v) == 4 for v in set(values)):
            return cls(cards)


class StraightFlush(Combination):
    rank = 9

    def same_rank_compare(self, other: 'Combination'):
        m1 = min(c.value for c in self.cards)
        m2 = min(c.value for c in other.cards)

        return self.compare_values(m1, m2)

    @classmethod
    def create(cls, cards: Sequence[Card]):
        if len(set(c.suite for c in cards)) == 1 and "".join(
                sorted((c.value for c in cards), key=CARD_VALUE.index)
        ) in CARD_VALUE + CARD_VALUE:
            return cls(cards)


class RoyalFlush(Combination):
    rank = 10

    def same_rank_compare(self, other: 'Combination'):
        return TIE

    @classmethod
    def create(cls, cards: Sequence[Card]):
        if len(set(c.suite for c in cards)) == 1 and CARD_VALUE.endswith("".join(sorted(c.value for c in cards))):
            return cls(cards)


COMBINATIONS = list(sorted(Combination.__subclasses__(), key=lambda cls: cls.rank, reverse=True))


def get_combination(cards: Sequence[Card]):
    return next(c for c in (cls.create(cards) for cls in COMBINATIONS) if c)


class PokerHand(object):

    def __init__(self, hand):
        self.cards = [Card(value, suite) for value, suite in hand.split()]

    def compare_with(self, other: 'PokerHand'):
        c1 = get_combination(self.cards)
        c2 = get_combination(other.cards)

        return c1.compare(c2)
