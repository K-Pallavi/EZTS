#recursion FAB series
def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
if __name__=="__main__":
    n=int(input("enter the number: "))
    print(fib(n,))
    
    