#Program to accept user input, put it in list and split numeric value to display in a new List
a = input("Enter the Number : ")
list1=[]
list2=[]
b = int(a)
for x in range(b):
    w = input("Enter List item : ")
    list2.append(w)
    if w.isdigit(): #works only for String Data
        list1.append(w)
else:
        print("End of Data Insertion")
        
print("The Final List is")
for x in list2:
    print(x)
  
print("Only Integer values are displayed")      
for x in list1:
    print(x)
    