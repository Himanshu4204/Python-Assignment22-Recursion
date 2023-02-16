#10. Write a recursive python function to find the Nth term of the Fibonacci series.?
def fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n=int(input("Enter a Number :"))
x=fibonacci(n)
print(n,"th Term is :",x)
