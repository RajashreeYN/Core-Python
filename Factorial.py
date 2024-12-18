#Q.1)WAP to get factorial of a number using function
def factorial(n):
    if n<=0:
        return "factorial is not defined as it is negative number"
    elif n==0:
        return 1
    else:
        fact=1
        for i in range(1,n+1):
         fact*=i
        return fact
num =int(input("Enter the value of n"))
result=factorial(num)
print(f"the factorial of { num} is { result}")
