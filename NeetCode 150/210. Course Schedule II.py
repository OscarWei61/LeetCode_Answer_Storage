class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        result = []
        prematrix = [[] for _ in range(numCourses)]
        num_pre = [0] * numCourses

        for course, precourse in prerequisites:
            num_pre[course] = num_pre[course] + 1
            prematrix[precourse].append(course)
        
        approve_course_list = deque([i for i in range(numCourses) if num_pre[i] == 0])

        while approve_course_list:
            course = approve_course_list.pop()
            result.append(course)

            for depent_course in prematrix[course]:
                num_pre[depent_course] = num_pre[depent_course] - 1
                
                if num_pre[depent_course] == 0:
                    approve_course_list.append(depent_course)
        
        if len(result) == numCourses:
            return result
        else:
            return []
                

