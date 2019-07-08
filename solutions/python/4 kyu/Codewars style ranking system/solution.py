RANKS = [i for i in range(-8, 8 + 1) if i]


class User:
    def __init__(self):
        self.rank = RANKS[0]
        self.progress = 0

    def inc_progress(self, rank):
        assert rank in RANKS

        if RANKS.index(self.rank) - RANKS.index(rank) > 1 or self.rank == RANKS[-1]:
            return
        elif RANKS.index(self.rank) - RANKS.index(rank) == 1:
            self.progress += 1
        elif rank == self.rank:
            self.progress += 3
        else:
            d = RANKS.index(rank) - RANKS.index(self.rank)
            self.progress += 10 * d * d

        self.rank = RANKS[min(RANKS.index(self.rank) + self.progress // 100, len(RANKS))]
        self.rank = min(self.rank, 8)
        self.progress = self.progress % 100 * (self.rank != RANKS[-1])
