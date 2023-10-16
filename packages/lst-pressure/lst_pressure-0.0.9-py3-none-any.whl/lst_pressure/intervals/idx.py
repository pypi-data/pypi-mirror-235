from intervaltree import IntervalTree, Interval


class Idx:
    def __init__(self):
        self.idx = IntervalTree()
        self.tree = self.idx
    
    def get_entries(self):
        return self.idx.items()

    def insert(self, begin, end, interval):
        try:
            self.idx[begin:end] = interval
        except Exception as e:
            raise Exception(f"Unable to insert interval. BEGIN: {begin} END {end}")

    def get_intervals_contained_by(self, *args):
        return self.idx.envelop(*args)

    """
    intervaltree doesn't have a direct query for intervals contained
    by some interval. Instead first get all intervals that overlap
    with the query, and filter the results where the query is completely
    contained. This is still efficient
    """
    def get_intervals_containing(self, *args):
        return [
            interval
            for interval in self.idx.overlap(*args)
            if interval.contains_interval(Interval(*args))
        ]
