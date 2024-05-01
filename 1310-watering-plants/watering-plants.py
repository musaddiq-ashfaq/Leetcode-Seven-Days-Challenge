class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        steps = 0
        i = 0
        full = capacity
        while(i<len(plants)):
            print(steps)
            if(capacity>=plants[i]):
                steps+=1
                capacity-=plants[i]
                i+=1
            else:
                steps = steps + i
                capacity = full
                steps = steps + i
        return steps