class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}

        for Course in range(numCourses):
            graph[Course] = []

        for pair in prerequisites:
            graph[pair[0]].append(pair[1])
        courses = [i for i in range(numCourses)]
        def availabe(graph):
            for el in graph:
                if not graph[el]:
                    return el
            return None
        """print(graph,courses) """
        while courses:
            course = availabe(graph)
            """print("course",course)"""
            if course == None:
                return False
            else:
                
                for el in graph:
                    if course in graph[el]:
                        graph[el].remove(course)
                if not graph[course]:
                    try:
                        graph.pop(course)
                        courses.remove(course)
                    except:
                            pass
                
            """print(graph,courses)"""

            

        return True