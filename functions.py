def check_passing(grade):
    if grade >= 60:
        return "Passed"
    else:
        return "Try again"

grades = [85, 52, 90]
for g in grades:
    print(g, "-", check_passing(g))
