marks_maths = float(input("Enter the marks in Maths: "))
marks_physics = float(input("Enter the marks in Physics: "))
marks_chemistry = float(input("Enter the marks in Chemistry: "))
if marks_maths < 35 or marks_chemistry < 35 or marks_physics < 35:
    # failed
    failed_subjects = []
    if marks_maths < 35:
        failed_subjects.append("Maths")
    if marks_physics < 35:
        failed_subjects.append("Physics")
    if marks_chemistry < 35:
        failed_subjects.append("Chemistry")
    print(f"Sorry! You are failed in {failed_subjects}")
else:
    # pass
    marks_avg = (marks_maths + marks_physics + marks_chemistry)/3
    if marks_avg > 69:
        print("Congrats! You are passed with Grade: A")
    elif marks_avg > 59:
        print("Congrats! You are passed with Grade: B")
    else:
        print("Congrats! You are passed with Grade: C")
    # if/else ends here
# if/else ends here
