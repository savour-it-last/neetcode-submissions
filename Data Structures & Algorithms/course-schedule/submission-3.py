class Solution:
    def check_if_revisiting(self, course: int, depMap: dict[int, list[int]]) -> bool:
        """
        Check if the course was already visited
        """
        if course in self.visited:
            return False
        if depMap[course] == []:
            return True
        self.visited.add(course)
        for pre in depMap[course]:
            if not self.check_if_revisiting(course=pre, depMap=depMap):
                return False
        # Unwind path values for the next path to check if its not False
        self.visited.remove(course)
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        depMap = {i: [] for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            depMap[course].append(prerequisite)

        for course in range(numCourses):
            self.visited = set()
            if not self.check_if_revisiting(course=course, depMap=depMap):
                return False
        return True
