# write a recursive python function to calculate sum of square of first N natural Number ?
def square_sum(n):
    if n==1:
        return 1
    else:
        return n**2+square_sum(n-1)
n=int(input("Enter how many numbers sum you want :"))
x=square_sum(n)
print(x)