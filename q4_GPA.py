def gpa_calculator(grades: list[int]) -> str:
    total_scor = 0
    number_of_scores = len(grades)
    for grade in grades:
        if grade > 20 or grade < 0:
            return "invalid score!"
        else:
            total_scor += grade
            
    gpa = total_scor / number_of_scores
     
    if gpa >= 18:
        return "A"
    elif gpa >= 15:
        return "B"
    elif gpa >= 12:
        return "C"
    else:
        return "F"
    
# با یک فاصله بین هر نمره وارد کنید
grades = input("enter 5 grades: ").split()
# تبدیل اعضا به عدد
grades = list(map(float, grades))

print(gpa_calculator(grades=grades))