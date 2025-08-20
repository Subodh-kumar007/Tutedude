#Calculate Factorial Using recursion
def factorial(num):
    if num<2:
        return 1
    else:
        return num * (factorial(num-1))



#Calculate Factorial Using loop
# def factorial(number):
#     num=number
#     f=1
#     while num>0:
#         f=f*num
#         num-=1
#     return f
number=int(input("Enter the Number: "))
fac=factorial(number)
print(f"factorial of {number} is: {fac}")



