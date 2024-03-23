#HashTable:-
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class HashTable:
    def __init__(self,size):
        self.table=[None]*size
        self.size=size
    def hash(self,data):
        return data%self.size
    def insert(self,data):
        key=ob.hash(data)
        newnode=Node(data)
        if(self.table[key]==None):
            self.table[key]=newnode
        else:
            temp=self.table[key]
            while(temp.next!=None):
                temp=temp.next
            temp.next=newnode
    def search(self,data):
        key=ob.hash(data)
        temp=self.table[key]
        if(temp==None):
            return "no data"
        while(temp!=None):
            if(temp.data==data):
                return temp.data
            temp=temp.next
        return "data is not present"
    def display(self):
        for i in range(self.size):
            temp=self.table[i]
            while(temp!=None):
                print(temp.data,end=" ")
                temp=temp.next
    def delete(self,data):
        key=ob.hash(data)
        temp=self.table[key]
        if(temp==None):
            return "no data"
        if(temp.data==data):
            self.table[key]=temp.next
            return data
        t1=temp
        t2=t1.next
        while(t2!=None):
            if(t2.data==data):
                t1.next=t2.next
                return data
            t2=t2.next
            t1=t1.next
        return "data is not present"
n=int(input("Enter the table size"))
ob=HashTable(n)
n=int(input("press\n 1 to insert\n 2 to delete\n 3 to display\n 4 to search \n other\
to exit"))
while(True):
    if(n==1):
        data=int(input("Enter the data to be inserted"))
        ob.insert(data)
        print(data,"is inserted")
    elif(n==2):
        data=int(input("Enter the data to be deleted"))
        print(ob.delete(data),"is deleted")
    elif(n==3):
        print("Elements in table are:- ")
        ob.display()
    elif(n==4):
        data=int(input("Enter the data"))
        print(ob.search(data),"is present")
    else:
        break                                       #github.com/Anand-29
        
    
