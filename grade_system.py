# Student Grade Management System
# This program stores student marks, calculates average, and assign grades.

students = {
    "Ravi": [78, 85, 90],
    "Sita": [88, 79, 92],
    "Lisa": [60, 70, 99]
}

print("STUDENT GRADE REPORT")
print("---------------------")

for name, marks in students.items():

    # Calculate total marks
    total = sum(marks)

    # Calculate average
    average = total / len(marks)

    # Assign grade based on average
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade  = "D"

    # Display student result
    print("Student Name: ", name)
    print("Marks       : ",marks)
    print("Average     : ",round(average,2))
    print("Grade       : ",grade)
    print("--------------------")
    