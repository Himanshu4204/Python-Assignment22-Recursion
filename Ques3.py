#Write a recursive python function to calculate the sum of first N even natural Numbers ?
def sum_even(n):
    if n==1:
        return 2
    else:
        return n*2+sum_even(n-1)
n=int(input("Enter how many numbers sum you want :"))
x=sum_even(n)
print(x)