class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        answer, remain = 0, capacity
        for loc, p in enumerate(plants):
            if remain < p:
                # Refill
                answer += 2 * loc
                remain = capacity
            remain -= p
            answer += 1
        return answer
