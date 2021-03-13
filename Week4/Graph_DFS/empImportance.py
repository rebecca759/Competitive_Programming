"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        return self.dfs(employees,id,0,0)
        
        
    def dfs(self,employees,id,imp,t):
        imp = 0
        
        for i in range(len(employees)):
            if employees[i].id == id:  
                imp += employees[i].importance
                
                for ids in employees[i].subordinates:
                    imp += self.dfs(employees,ids,imp,t)
        
        t += imp
        return t
