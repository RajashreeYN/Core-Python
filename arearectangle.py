def calculate_area(length, width):
  area = length * width  #calculate area of rectangle
  return area

if __name__ == "__main__":
  length = float(input("Enter the length of the rectangle: "))
  width = float(input("Enter the width of the rectangle: "))

  area = calculate_area(length, width)
  print("The area of the rectangle is:", area)
