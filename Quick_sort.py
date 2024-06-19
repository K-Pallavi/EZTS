def divide(L,Low,High):
    P=L[High]
    pi=High
    j=Low-1
    for i in range(Low,High):
        if L[i]<=P:
            j+=1
            L[i],L[j]=L[j],L[i]
    j+=1
    L[j],L[pi]=L[pi],L[j]
    pi=j
    return pi
def quick_sort(L,Low,High):
    if Low<High:
        pi=divide(L,Low,High)
        print(pi,Low,High)
        quick_sort(L,Low,pi-1)
        quick_sort(L,pi+1,High)
    return
if __name__=="__main__":
    L=list(map(int,input("enter the elements to be sorted: ").split()))
    Low=0
    High=len(L)-1
    print(Low,High)
    quick_sort(L,Low,High)
    print("sorted Array: ",L)