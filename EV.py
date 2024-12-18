def is_even(number):
  return number % 2 == 0  
if __name__ == "__main__":
  number = int(input("Enter a number: "))
  if is_even(number):
    print(number, "is even.")
  else:
    print(number, "is odd.")
