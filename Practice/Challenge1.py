#Method to accept list and separate Integer to store in a new List
def integerList(aList):
    list1=[]
    for x in aList:
        if isinstance(x, int):
            list1.append(x)
    else:
        print("The List is Complete")
    
    for x in list1:
    	print(x)
        
aList=["Hello",14,"13",15.5,15]
integerList(aList)