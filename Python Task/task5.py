# 5. Listin içində təkrarlanan elementləri tapın
myList=[1,34,56,100,-12,87,987,1,3,5,56,67]

newList=[x for x in myList if myList.count(x)!=1]
for x in newList:
    print(x)