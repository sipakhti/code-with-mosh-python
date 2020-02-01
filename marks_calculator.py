def grader(subject_marks, total_marks=150):
    if 50 <= ((subject_marks * 100) / total_marks) < 60:
        return "E"
    if 60 <= ((subject_marks * 100) / total_marks) < 70:
        return "D"
    if 70 <= ((subject_marks * 100) / total_marks) < 80:
        return "C"
    if 80 <= ((subject_marks * 100) / total_marks) < 90:
        return "B"
    if 90 <= ((subject_marks * 100) / total_marks):
        return "A"
    return "F"


marks = {"english": 0, "islamiat": 0, "pakistan_studies": 0, "physics": 0, "biology": 0, "math": 0, "urdu": 0, "total_obtained": 0}
subjects = ("english", "islamiat","pakistan_studies","physics","biology","math","urdu")

for subject in subjects:
    marks[subject] = int(input(f"Please enter {subject} marks: "))
    print(type(marks[subject]))
    while not (0 <= marks[subject] <= 150):
        print("Invalid marks!!! \n choose any number between 0 - 150")
        marks[subject] = int(input(f"Please enter {subject} marks: "))
       

for subject in subjects:
    print(f"{subject}: {marks[subject]} grade:{grader(marks[subject])}")
    marks["total_obtained"] += marks[subject]

print(f"TOTAL: {marks['total_obtained']}  grade:{grader(marks['total_obtained'],1050)}")


