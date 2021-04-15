a=input()
b=input()
x=input()
y=input()
if((len(x)==4 and len(y)==7) or (len(x)==7 and len(y)==5) or(len(x)==5 and len(y)==4)):
   print(f"{a} Win")
else:
   print(f"{b} Win")