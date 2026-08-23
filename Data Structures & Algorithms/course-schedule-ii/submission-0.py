class Solution:
    def can_take_course(self, course_mapping: dict[int, list[int]], course: int)->bool:
        if course in self.visiting:
            return False
        
        if course in self.visited:
            return True

        self.visiting.add(course)
        
        for pre in course_mapping[course]:
            if not self.can_take_course(
            course_mapping=course_mapping, 
            course=pre
            ):
                return False
            
        self.visited.add(course)
        self.schedule.append(course)
        self.visiting.remove(course)
        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_mapping = {i: [] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            course_mapping[course].append(prerequisite)

        self.visited = set()

        self.schedule = []
        for course in range(numCourses):
            self.visiting = set()
            if not self.can_take_course(course_mapping=course_mapping, course=course):
                return []
            self.visited.add(course)
        return self.schedule





            
            

        
        

