n=int(input())
vi=bin(n).replace("0b","")
svi=str(vi)
svi1=len(svi)
for i in range(0,n+1):
    mo=(bin(i).replace("0b",""))
    moi=str(mo)
    moi1=len(moi)
    if(moi1<svi1):
        for j in range(0,svi1-moi1):
            print(" ",end=" ")
        print(mo) 