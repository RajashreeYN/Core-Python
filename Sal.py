#Q.4) WAP to accept basic salary from user and Give 10% of DA on basic salary ,12% HRA on basic salary  to employee if the salary is more than 50000 .calculate total salary.
def calculate_total_salary(basic_salary):
  if basic_salary > 50000:
    da = basic_salary * 0.1  # 10% DA
    hra = basic_salary * 0.12  # 12% HRA
    total_salary = basic_salary + da + hra
  else:
    total_salary = basic_salary  # No DA or HRA for salaries less than 50000
  return total_salary
if __name__ == "__main__":
  basic_salary = float(input("Enter the basic salary: "))
  total_salary = calculate_total_salary(basic_salary)
  print("The total salary is:", total_salary)
