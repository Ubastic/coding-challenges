from math import ceil, floor


class PaginationHelper:

    def __init__(self, collection, items_per_page):
        collection = list(collection)
        self._page_size = items_per_page
        self._items_count = len(collection)
        self._page_count = int(ceil(float(self._items_count) / items_per_page))

    def __repr__(self):
        return '{} {} {}'.format(self._page_size, self._items_count, self._page_count)

    def item_count(self):
        return self._items_count

    def page_count(self):
        return self._page_count

    def page_index(self, item_index):
        if item_index >= self._items_count or item_index < 0:
            return -1

        return int(floor(floor(item_index) / self._page_size))

    def page_item_count(self, page_index):
        if not (0 < page_index < self._page_count):
            return -1

        if page_index == self._page_count - 1:
            return self._items_count % self._page_size

        return self._page_size