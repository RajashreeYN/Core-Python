students = {                #Creating Dictionary
    "Nirmal": "A",
    "Ray": "C",
    "Riya": "A",
    "Priya": "A",
    "Star": "B"
}
print("Students and their Grades:")    #DisplayingDictionary
for student, grade in students.items():
    print(f"{student}: {grade}")
students["Mahi"] = "A"      #Adding new student
print("\nAfter adding Mahi:")
print(students)
students["Star"] = "A"   # Updating grades of one student
print("\nAfter updating Star's grade:")
print(students)
del students["Priya"]   #Removing student
print("\nAfter removing Priya:")
print(students)
student_to_check = "Iyara" # Checkong if student exist in dictionary
if student_to_check in students:
    print(f"\n{student_to_check} is in the list with grade {students[student_to_check]}")
else:
    print(f"\n{student_to_check} is not in the list") #displaying all studnts
print("\nAll students:")
for student in students.keys():
    print(student)
print("\nAll grades:") #Displaying all grades
for grade in students.values():
    print(grade)
