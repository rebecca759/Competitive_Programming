# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return ""

        res = ""
        queue = deque([(0,root,"")])

        while queue:
            cur_level,node,d = queue.popleft()
            val = node.val if node else "*"
            res += (str(cur_level)+","+str(val)+","+d+".")
            if node:
                queue.append((cur_level+1,node.left,"L"))
                queue.append((cur_level+1,node.right,"R"))
        
        return res[:len(res)-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return

        data = data.split(".")
        for i in range(len(data)):
            data[i] = data[i].split(",")

        root = TreeNode(data[0][1])
        queue = deque([(0,root)])
        ind = 1

        while ind < len(data) and queue:
            level,node = queue.popleft()
            if int(data[ind][0]) > level:
                if data[ind][1] == "*":
                    new_node = None
                else:
                    new_node = TreeNode(int(data[ind][1]))
                if data[ind][2] == "L":
                    node.left = new_node
                else:
                    node.right = new_node

                if new_node:
                    queue.append((level+1,new_node))

            ind += 1

            if ind < len(data) and int(data[ind][0]) > level:
                if data[ind][1] == "*":
                    new_node = None
                else:
                    new_node = TreeNode(int(data[ind][1]))
                node.right = new_node
                if new_node:
                    queue.append((level+1,new_node))
                ind += 1

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))