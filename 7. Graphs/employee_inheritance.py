"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mapping = {i.id: i for i in employees}
        def dfs(emp):
            cur = mapping[emp]
            return cur.importance + (sum(dfs(emp) for emp in cur.subordinates))
        return dfs(id)
