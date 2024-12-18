def calculate_average(num1, num2, num3):
  
  average = (num1 + num2 + num3) / 3     # average of three numbers
  return average

if __name__ == "__main__":       # Get user input for the three numbers
  num1 = float(input("Enter the first number:"))
  num2 = float(input("Enter the second number:"))
  num3 = float(input("Enter the third number:"))
  average = calculate_average(num1, num2, num3)
  print("The average of the three numbers is:", average) #print
