a=0
b=1
n=int(input("enter number of terms:"))
print("fibonacci series:")
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    
