# Write a recursive python function to calculate sum of first N odd natural numbers?
def sum_odd(n):
    if n>0:
        print(n+(n-1))
        sum_odd(n-1)
n=int(input("Enter how many numbers sun you want :"))
sum_odd(n)
        