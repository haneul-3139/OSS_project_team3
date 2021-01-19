class Fibonacci:
    def __init__(self,title="fibonacci"):
        self.title= title
    def fib(n):
        a,b, = 0,1
        while a<n:
            a, b = b, a+b
            print(a,end=' ')   
        print()

    def fib2(n):
        result=[]
        a,b = 0,1
        while a<n:
            a,b = b, a+b
            result.append(a)
        return result