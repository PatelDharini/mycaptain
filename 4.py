#to print all the positive numbers from the list provided by user
l=[]
n=int(input('Enter the number of elements f0r list:'))
for i in range(0,n):
    element=int(input())
    l.append(element)
print("The list is:",l)
print("output:",end="")
for i in l:
    if i>=0:
        print(i, end="  ")
   
      
