# Write a recursive python function to calculate sum of first N natural numbers ?
def sum_naturals(n):
    if n == 1:
        return 1
    else:
        return n + sum_naturals(n-1)
n=int(input("Enter how many numbers sum you want :"))
x=sum_naturals(n)
print(x)
