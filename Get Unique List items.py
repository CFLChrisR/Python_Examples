#Grab Unique list values
NewList =[3,6,1,2,5,9,6,1,7,5]
listtwo=[]
for nl in NewList:
    if nl not in listtwo:
        listtwo.append(nl)
print(sorted(listtwo))
print (sorted(NewList))