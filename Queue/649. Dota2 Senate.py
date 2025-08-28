class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        self.queuer = deque()
        self.queued = deque()
        
        for index in range(0, len(senate)):
            if senate[index] =="R":
                self.queuer.append(index)
            else:
                self.queued.append(index)
        
        while len(self.queuer) > 0 and len(self.queued) > 0:
            if self.queuer[0] < self.queued[0]:
                self.queued.popleft()
                self.queuer.append(self.queuer[0] + len(senate))
                self.queuer.popleft()
            else:
                self.queuer.popleft()
                self.queued.append(self.queued[0] + len(senate))
                self.queued.popleft()
            
        if len(self.queued) == 0:
            return "Radiant"
        else:
            return "Dire"