def check_passing(grade):
    if grade >= 60:
        return "Passed"
    else:
        return "Try again"

grades = [85, 52, 90]
for grade in grades:
    print(grade, "-", check_passing(g))
