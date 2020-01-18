class Solution:
    def canFinish(self, numCourses: int, prereq: List[List[int]]) -> bool:
        outdegree = {}
        indegree = {}
        
        for i in prereq:
            if i[0] not in outdegree:
                outdegree[i[0]] = 1
            else:
                outdegree[i[0]] +=1
        
        for j in prereq:
            if j[1] not in indegree:
                indegree[j[1]]=[j[0]]
            else:
                indegree[j[1]].append(j[0])
                 
        #print(outdegree)
        #print(indegree)
        queue = []
        for i in range (numCourses):
            if i not in outdegree:
                queue.append(i)
        sol = 0
        while queue:
            sol +=1
            x = queue.pop(0)
            if x in indegree:
                for c in indegree[x]:
                    outdegree[c] -= 1
                    if outdegree[c] == 0:
                        del outdegree[c]
                        queue.append(c)
        
        return sol == numCourses
        
    
                
                
        
