class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None


    #Insert method
    def insert(data):
        if self.data:
            if self.data <= data:
                if not self.left:
                    self.left = Node(data)
                    return

                else:
                    self.left.insert(data)

            elif self.data > data:
                if not self.right:
                    self.right = Node(data)

                else:
                    self.right.insert(data)

        else:
            self.data = data


    #Find method
    def find(data):
        if self.data:
            if self.data < data:
                if self.left:
                    return self.left.find(data)
                else:
                    return -1

            elif self.data > data:
                if self.right:
                    return self.right.find(data)

                else:
                    return -1

            elif self.data == data:
                return data

    #Delete method
    def delete(data):
        if self.data:
            if self.data < data:
                if self.left:
                    self.left.delete(data)

                else:
                    return

            elif self.data > data:
                if self.right:
                    self.right.delete(data)

                else:
                    return

            else:
                #delete
                if self.left:
                    self.left.data, self.data = self.data, self.left.data
                    self.left = self.left.left
                    self.right = self.left.right

                elif self.right:
                    self.right.data, self.data = self.data, self.right.data
                    self.right = self.right.right
                    self.left = 
                    
                    

        else:
            return

                
            

                
        
