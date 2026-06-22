import heapq
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        heapq.heapify(costs)
        count = 0
        while coins > 0 and costs:
            now = heapq.heappop(costs)
            if coins - now >= 0:
                count += 1
                coins -= now
            else:
                break
        return count