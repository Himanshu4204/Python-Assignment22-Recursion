# write a recursive python function to print octal of a given decimal number ?
def change_octal(n):
    if n<8:
        return str(n)
    else:
        return change_octal(n//8)+str(n%8)
n=int(input("Enter a Number :"))
x=change_octal(n)
print(x)
