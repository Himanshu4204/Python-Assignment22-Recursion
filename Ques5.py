#write a recursive python function to calculate the sum of cubes of first N natural Numbers ?
def cubes_sum(n):
    if n==1:
        return 1
    else:
        return n**3+cubes_sum(n-1)
n=int(input("Enter how many numbers sum you want :"))
x=cubes_sum(n)
print(x)
