# 6. Listin içindən tək yerdə duran elementləri silərək əldə olunan listi ekrana çap edin
myList=[1,34,56,100,-12,87,987,1,3,5,56,67]

newList=[x for x in myList if myList.index(x)%2==1]

def Foo():
    for i in range(len(newList)):
        myList.remove(newList[i])
Foo()
[print (x) for x in myList]

