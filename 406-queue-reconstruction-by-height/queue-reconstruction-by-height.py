class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        reconstructed_queue = []
    
        for p in people:
            reconstructed_queue.insert(p[1], p)
        return reconstructed_queue
