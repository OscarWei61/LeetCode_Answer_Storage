class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        
        result = []
        for speed in asteroids:
            remaining = True

            while result and remaining and result[-1] > 0 and speed < 0:
                top_item = result[-1]

                if top_item < (-1 * speed):
                    result.pop()

                elif top_item == (-1 * speed):
                    remaining = False
                    result.pop()
                    break
                
                else:
                    remaining = False
                    break
            
            if remaining == True:
                result.append(speed)
        
        return result