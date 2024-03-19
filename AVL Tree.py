class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.ht=1
class Tree:
    def insert(self,root,data):
        #insert the node a relevant position
        if(root==None):
            newnode=Node(data)
            return newnode
        elif(data<root.data):
            root.left=ob.insert(root.left,data)
        elif(data>root.data):
            root.right=ob.insert(root.right,data)
        
        #update the height of each node
        root.ht=1+max(ob.getheight(root.left),ob.getheight(root.right))
        
        #find balancing factor
        balance=ob.balancing(root)
        
        #balance is positive check for LL or LR
        if(balance>1):
            if(data<root.left.data):
                return ob.rightrotate(root)
            else:
                root.left=ob.leftrotate(root.left)
                return ob.rightrotate(root)
        
        #balance is negative check for RR or RL
        if(balance<-1):
            if(data>root.right.data):
                return ob.leftrotate(root)
            else:
                root.right=ob.rightrotate(root.right)
                return ob.leftrotate(root)
        return root
        
    #fun for getting height
    def getheight(self,root):
        if(root==None):
            return 0
        else:
            return root.ht
    
    #get balancing factor
    def balancing(self,root):
        if(root==None):
            return 0
        else:
            bfactor=ob.getheight(root.left)-ob.getheight(root.right)
            return bfactor
            
    def preorder(self,root):
        if(root==None):
            return 
        print(root.data,end="->")
        ob.preorder(root.left)
        ob.preorder(root.right)
    
    def rightrotate(self,root):
        t1=root.left
        t2=t1.right
        root.left=t2
        t1.right=root
        root.ht=1+max(ob.getheight(root.left),ob.getheight(root.right))
        t1.ht=1+max(ob.getheight(t1.left),ob.getheight(t1.right))
        return t1
    
    def leftrotate(self,root):
        t1=root.right
        t2=t1.left
        root.right=t2
        t1.left=root
        root.ht=1+max(ob.getheight(root.left),ob.getheight(root.right))
        t1.ht=1+max(ob.getheight(t1.left),ob.height(t1.right))
        return t1
    
    def verify(self,root):
        if(root==None):
            return False
        if(root.right!=None):
            return True
        else:
            return ob.verify(root.left)
    
    def height(self,root):
        if(root==None):
            return 0
        else:
            if(ob.height(root.left)>ob.height(root.right)):
                return 1+ob.height(root.left)
            else:
                return 1+ob.height(root.right)
ob=Tree()
root=None
root=ob.insert(root,5)
root=ob.insert(root,3)
root=ob.insert(root,4)
ob.preorder(root)
print()
print(ob.height(root))
