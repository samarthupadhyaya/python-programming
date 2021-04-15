#using while loop 
n=input()
ln=len(n)
s=0
i=0
while(i<ln):
    print(n[i])
    s+=int(n[i])**ln
    i+=1
if int(n)==s:
    print("armstrong")
else:
    print("not an armstrong number")



















# using for loop

#a=raw_int(input("enter the number"))
#ln=len(a)
#s=0
#for i in a:
 #   s+=int(i)**ln
#if int(a)==s:
 #   print("number is armstrong")
#else:
 #   print("not an armstrong number")