#Q.1) WAP to find greatest among two numbers 
def find_greatest(num1, num2):    #Finds the greatest of two numbers.
  if num1 > num2:
    return num1
  else:
    return num2

if __name__ == "__main__":
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))

  greatest_num = find_greatest(num1, num2)
  print("The greatest number is:", greatest_num)
