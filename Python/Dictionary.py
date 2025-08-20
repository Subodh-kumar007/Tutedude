student_marks={"Alice":85,"Bob":92,"Charlie":78,"David":95,"Ram":45}
# print(student_marks)
sname=input("Enter the Student Name: ")
if sname in student_marks:
    print(f"{sname} marks is : {student_marks[sname]}")
else:
    print("Student Not Found")

