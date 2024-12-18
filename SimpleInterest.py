#Q.1)WAP to calculate simple interest.
def simple_interest(p, t, r):
    si = (p * t * r) / 100   #FORMULA
    return si
if __name__ == "__main__":
    principal = float(input("Enter the principal amount: "))
    time = float(input("Enter the time period (in years): "))
    rate = float(input("Enter the rate of interest: "))
    interest = simple_interest(principal, time, rate)
    print("The simple interest is:", interest)
