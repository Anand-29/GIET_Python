#HashTable
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Hash:
    def __init__(self,size):
        self.table=[None]*size
        self.size=size
    def hash(self,data):
        return data%self.size
    def insert(self,data):
        index=ob.hash(data)
        newnode=Node(data)
        if(self.table[index]==None):
            self.table[index]=newnode
        else:
            temp=self.table[index]
            if(temp.next!=None):
                temp=temp.next
            temp.next=newnode
    def search(self,data):
        index=ob.hash(data)
        temp=self.table[index]
        flag=0
        while(temp!=None):
            if(temp.data==data):
                flag=1
                return temp.data
            temp=temp.next
        if(flag==0):
            return "no data is present"
    def display(self):
        print()
        for i in range(self.size):
            temp=self.table[i]
            while(temp!=None):
                print(temp.data,end=" ")
                temp=temp.next
    def delete(self,data):
        index=ob.hash(data)
        temp=self.table[index]
        if(temp==None):
            return -1
        if(temp.data==data):
            self.table[index]=temp.next
            return temp.data
        else:
            t1=temp
            t2=t1.next                  
            while(t2!=None):
                if(t2.data==data):
                    t1.next=t2.next
                    return t2.data
                t2=t2.next
                t1=t1.next
            if(t2==None):
                return -1
                
ob=Hash(10)
while(True):
    print("press 1 to insert\n2 to delete\n3 to display\n other to exit")
    n=int(input())
    if(n==1):
        data=int(input("\nenter the data"))
        ob.insert(data)
    elif(n==2):
        data=int(input("\nenter the data"))
        if(ob.delete(data)<0):
            print("\n",data,"is deleted")
        else:
            print("\n",data,"is not present")
    elif(n==3):
        ob.display()
    else:
        break               #github.com/Anand-29
