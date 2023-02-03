# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        self.traverse(root,0,0,dic)
        res = []
        heap = list(dic.keys())
        heapq.heapify(heap)

        while heap:
            col = heapq.heappop(heap)
            res.append([])
            dic[col] = sorted(dic[col])
            for r,val in dic[col]:
                res[-1].append(val)

        return res

    def traverse(self,node,r,c,dic):
        if not node:
            return

        dic[c].append((r,node.val))

        self.traverse(node.left,r+1,c-1,dic)
        self.traverse(node.right,r+1,c+1,dic)