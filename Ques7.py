# write a recursive python function to calculate sum of the digits of a given number ?
def sum_digit(n):
    if n<10:
        return n
    else:
        return n%10+sum_digit(n//10)
n=int(input("Enter some numbres :"))
x=sum_digit(n)
print(x)

