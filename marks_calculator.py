def grader(subject_marks, total_marks=150):
    """Calculates Grades and returns the grade"""

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


marks = {"english": 0, "islamiat": 0, "pakistan_studies": 0,
         "physics": 0, "biology": 0, "math": 0, "urdu": 0, "total": 0}
subjects = ("english", "islamiat", "pakistan_studies",
            "physics", "biology", "math", "urdu")

# continous execution loop
while True:
    # so that the value doesnt stack up after every iteration of the loop
    marks["total"] = 0

    student_name = input("Enter student name:\n")

# Input Loop
    for subject in subjects:
        # prevents program from crashing in case no value is entered at all
        try:
            marks[subject] = int(input(f"Please enter {subject} marks: "))

            while not (0 <= marks[subject] <= 150):
                print("Invalid marks!!! \n choose any number between 0 - 150")
                marks[subject] = int(input(f"Please enter {subject} marks: "))
        except ValueError:
            marks[subject] = 0

# prints out the subjects marks on the console
    for subject in subjects:
        print(f"{subject}: {marks[subject]} grade:{grader(marks[subject])}")
        marks["total"] += marks[subject]

    print(f"TOTAL: {marks['total']}  grade:{grader(marks['total'],1050)}")
    print("TOTAL: {}  grade:{}".format(
        marks["total"], grader(marks["total"], 1050)))

# creates a cummulaive string containig all the student data seperated by comma to be parsed in a database
    name = f"\r{student_name}"
    sub = ""
    for subject in subjects:
        sub += f",{marks.get(subject,0)}"
    total = f",{marks['total']},{grader(marks['total'],1050)}\n"

    complete_string = name + sub + total

# Saves the data to the file
    with open("student_data.txt", "a") as f_obj:
        f_obj.writelines(complete_string)

# option to break out of the loop
    exit_cmd = input(
        "Enter q to quit or anyother key to add marks for another student: ")
    if exit_cmd.lower() == "q":
        break
