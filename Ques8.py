#Write a recursive python function to print binary of a given decimal number.?
def decimal_to_binary(n):
    if n == 0:
        return ''
    else:
        return decimal_to_binary(n // 2)+str(n%2)
n=int(input("Enter a decimal number :"))
x=decimal_to_binary(n)
print(x)
