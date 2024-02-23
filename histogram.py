list=[2,3,5,2,1]
lb=[0]*5;rb=[0]*5
c=0
for i in range(0,5):
    c=0
    for j in range(i+1,5):
        if(list[j]>=list[i]):
            c+=1    
    rb[i]=c
    c=0
    for k in range(i-1,-1,-1):
        if(list[k]>=list[i]):
            c+=1    
    lb[i]=c
max=0
for i in range(0,5):
    if((lb[i]+rb[i]+1)*list[i]>=max):
        max=(lb[i]+rb[i]+1)*list[i]
print(max)
