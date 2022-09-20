#mycaptain program to print the fabonacci series.
n=int(input("enter the total number for fibonacci elements: "))
a=0
b=1
sum=0
count=1
print("Fibonacci series: ",end=" ")
while(count<=n):
    print(sum,end=" ")
    count+=1
    a=b
    b=sum
    sum=a+b
