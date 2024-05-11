import heapq


class Cabel:
    def __init__(self, id, length) -> None:
        self.id = id
        self.length = length

    def __lt__(self, other):
        return self.length < other.length


def merge_cabels_in_pairs(cabels):
    heap = []
    for value in cabels:
        heapq.heappush(heap, value)
    result = []
    sum = 0
    while len(heap) >= 2:
        shortest1 = heapq.heappop(heap)
        shortest2 = heapq.heappop(heap)
        sum += shortest1.length + shortest2.length
        result.append((shortest1.id, shortest2.id))
    if len(heap) == 1:
        result.append((heap[0].id, None))
        sum += heap[0].length
    return result, sum


def merge_cabels_into_one(cabels):
    if not cabels:
        return [], 0
    heap = []
    result = []
    for value in cabels:
        heapq.heappush(heap, value)
    while len(heap) >= 2:
        shortest1 = heapq.heappop(heap)
        shortest2 = heapq.heappop(heap)
        result.append((shortest1.id, shortest2.id))
        merged_cabel = Cabel(shortest1.id + shortest2.id,
                             shortest1.length + shortest2.length)
        heapq.heappush(heap, merged_cabel)

    return result, heap[0].length
