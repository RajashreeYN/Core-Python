def is_eligible_to_vote(age):  #Checks if a person is eligible to vote.
  return age >= 18
if __name__ == "__main__":
  age = int(input("Enter your age: "))

  if is_eligible_to_vote(age):
    print("You are eligible to vote.")
  else:
    print("You are not eligible to vote yet.")
