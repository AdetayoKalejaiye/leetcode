import heapq

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        #how I'd do it is to get the largest one less than the planet and then the smallest one more than the planet and alternate, now let's sanity check that
        # [3,9,19,5,21]  [9,19]  19, 38,
        bigger = [x for x in asteroids if x > mass]
        heapq.heapify(bigger)
        smaller = [x for x in asteroids if x <= mass]
        mass += sum(smaller)
        print(bigger)
        #what I'd do is as long as bigger is there if mass  > bigger[0], mass += bigger.heappop() else if smaller mass += -heapq.heappop(smaller) else break
        while bigger and mass >= bigger[0]:
            mass += heapq.heappop(bigger)
        if bigger:
            return False
        return True