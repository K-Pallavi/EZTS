#Tower Of Hannoi
def tower(n,frm,to,aux,ctr):
    if n==0:
        return
    tower(n-1,frm,aux,to,ctr)
    print(f"move {n} from {frm} to {to}")
    ctr[0]+=1
    tower(n-1,aux,to,frm,ctr)
ctr=[0]
n=3
tower(n,'a','c','b',ctr)
print(ctr)
