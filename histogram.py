list=[1,2,3,4,3,1,5]
lb=[0]*len(list);rb=[0]*len(list);c=0
for i in range(0,len(list)-1):
    c=0
    for j in range(i+1,len(list)):
        if(list[i]<=list[j]):
            c+=1
        else:
            break
    lb[i]=c
    c=0
    for k in range(i-1,-1,-1):
        if(list[i]<=list[k]):
            c+=1
        else:
            break
    rb[i]=c
    max=0
for i in range(0,len(list)):
    if((lb[i]+rb[i]+1)*list[i])>=max:
        max=(lb[i]+rb[i]+1)*list[i]
print(max)
    
