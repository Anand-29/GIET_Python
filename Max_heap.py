#heapify:-
def heap(arr,i,n):
    largest=i
    left=2*i+1
    right=2*i+2
    if(left<n and arr[left]>arr[i]):
        largest=left
    if(right<n and arr[right]>arr[largest]):
        largest=right
    if(largest!=i):
        arr[largest],arr[i]=arr[i],arr[largest]
        heap(arr,largest,n)
def insert(arr,data):
    if(len(arr)==0):
        arr.append(data)
    else:
        arr.append(data)
        for i in range((len(arr)//2)-1,-1,-1):
            heap(arr,i,len(arr))
def remove(arr):
    if(len(arr)==0):
        return "empty"
    else:
        data=arr[0]
        arr[0],arr[len(arr)-1]=arr[len(arr)-1],arr[0]
        arr.pop()
        for i in range((len(arr)//2)-1,-1,-1):
            heap(arr,i,len(arr))
        return data
def delete(arr,data):
    if(len(arr)==0):
        return "empty"
    else:
        flag=0;num=None
        for i in range(len(arr)):      #github.com/Anand-29
            if(arr[i]==data):
                flag=1
                break
        if(flag==1):
            num=arr[i]
        arr[i],arr[len(arr)-1]=arr[len(arr)-1],arr[i]
        arr.pop()
        for i in range(len(arr)-1,-1,-1):
            heap(arr,i,len(arr))
        return num
arr=[]
while(True):
    a=int(input())
    if(a<0):
        break
    insert(arr,a)
print(arr)
print("deleted->",delete(arr,2))
for i in range(len(arr)):
    print(remove(arr),end="->")


