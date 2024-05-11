import heapq
from copy import deepcopy


def merge_k_lists(lists):
    if not lists:
        return []
    result = []
    heap = []
    lists_to_merge = deepcopy(lists)
    while lists_to_merge:
        for list in lists_to_merge:
            if not list:
                lists_to_merge.remove(list)
                continue
            heapq.heappush(heap, list.pop(0))
        while heap:
            result.append(heapq.heappop(heap))
    return result


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
