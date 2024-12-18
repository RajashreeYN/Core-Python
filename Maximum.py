#Q.2)WAP to find maximum among two number
def find_max(num1, num2):    #Finds the maximum of two numbers.
    if num1 > num2:
        return num1
    else:
        return num2 
num1 = int(input("Enter the first number: "))    # Get input from the user
num2 = int(input("Enter the second number: "))
max_num = find_max(num1, num2)       #  maximum using the function
print("The maximum number is:", max_num)    #print
