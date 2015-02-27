class TreeNode:
        def __init__(self,  x):
                self.val = x
                self.left = None
                self.right = None

class Queue:
        def __init__(self):
                self.q = []
        
        def put(self, x):
              self.q.append(x)
                
        def get(self):
              return self.q.pop(0)

        def isEmpty(self):
                return len(self.q) == 0

        def peek(self, index):
                return self.q[index]



class Solution:
        # @param root, a tree node
        # @return a boolean
        def isSymmetric(self, root):                
                if root is None:
                        return True
                q = Queue()
                q.put(root.left)
                q.put(root.right)
                while True:
                        allEmpty = True
                        l = []
                        while not q.isEmpty():
                                #read from queue until its empty
                                l.append(q.get())
                
                        for x in range(0, len(l)-1):
                                #compare first of list to last of list
                                if l[x] is None and l[len(l)-1-x] is None:
                                        continue

                                compare1 = l[x].val if l[x] is not None else None
                                compare2 = l[len(l)-1-x].val if l[len(l)-1-x] is not None else None
                                if compare1 != compare2:
                                        return False

                        #put next tier into queue
                        print ("l length: " + str(len(l)))
                        for x in range(len(l)-1, -1, -1):
                                q.put(l[x].left if l[x] is not None else None)
                                q.put(l[x].right if l[x] is not None else None)
                        for x in range(0, len(l)-1):
                                if (q.peek(x) is not None):
                                        allEmpty = False

                        if allEmpty:
                                return True


s = Solution()

#init tree
root = TreeNode(1)
L1 = TreeNode(2)
L1.left = TreeNode(3)
L1.right = TreeNode(4)
R1 = TreeNode(2) 
R1.left = TreeNode(4)
R1.right = TreeNode(3)
root.left = L1
root.right = R1 
result = str(s.isSymmetric(root))
print(result)

