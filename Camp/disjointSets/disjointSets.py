class disjSets(self):
    def __init__(self):
        ''' ''''
        
        self.size = 5
        self.parent = [0]*size
        size = [0]*size

    def make_set(self):
        parent[v] = v
        size[v] = 1

    def find_set(self,v):
        if (v == parent[v]):
            return v
        return parent[v] = find_set(parent[v])

    def union_sets(self,a,b):
        a = find_set(a)
        b = find_set(b)
        
        if a != b:
            parent[b] = a

            
            
