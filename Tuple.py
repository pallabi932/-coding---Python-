a= (3, 4, 5) #when we use()=tuple
b=(3, 4, 5) #when we use[]=list
print ("original tuple:", a)
print("original tuple:", b)
a=(24, )+a[1：]
print (a)

a=[2, 24, 10, 12, 13, 3, 4, 34, 9, 8]
print (a[0:])
print (a[1:9:2])
print (a[-1])

Name= "my name is pallabi goswami"
print("palindrom" if Name==Name[::-1] else
"not palindrom")
