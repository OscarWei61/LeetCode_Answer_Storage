class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited_room = set([0])
        queue = deque([0])

        while queue:
            room = queue.popleft()
            for key in rooms[room]:
                if key not in visited_room:
                    visited_room.add(key)
                    queue.append(key)
        
        return len(visited_room) == len(rooms)
            
