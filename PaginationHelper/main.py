# TODO: complete this class


class PaginationHelper:

    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self) -> int:
        return len(self.collection)

    # returns the number of pages
    def page_count(self) -> int:
        count: int = self.item_count()
        return count // self.items_per_page + int(bool(count % self.items_per_page))

    def _split_into_chunks(self) -> list[int]:
        return [
            self.collection[i : i + self.items_per_page]
            for i in range(0, len(self.collection), self.items_per_page)
        ]

    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index: int) -> int:
        return (
            -1
            if (page_index > (self.page_count() - 1) or page_index < 0)
            else len(self._split_into_chunks()[page_index])
        )

    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index: int) -> int:
        if item_index < 0:
            return -1
        i = 0
        pages = self._split_into_chunks()
        for page_num, page in enumerate(pages):
            for _ in page:
                if i == item_index:
                    return page_num
                i += 1
        else:
            return -1
