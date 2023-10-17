class TodoPathData:
    id: int
    title: str | None = None
    will_be_completed_at: str | None = None
    completed_at: str | None


class GetTest:
    queue_range_str: str

    @property
    def queue_range(self) -> range:
        if self.queue_range_str == '1-10':
            return range(1, 10)
        n1, n2 = self.queue_range_str.split(',')
        return range(int(n1), int(n2))

