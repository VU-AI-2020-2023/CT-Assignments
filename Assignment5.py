
# Question 5
if __name__ == "__main__":
    gross_salary = float(input("What is your salary?\n"))

    if gross_salary < 10000:
        net_income = gross_salary
    elif gross_salary >= 10000 and gross_salary < 25000:
        net_income = gross_salary/10*9
    elif gross_salary >= 25000 and gross_salary < 50000:
        net_income = gross_salary/4*3
    elif gross_salary >= 50000:
        net_income = gross_salary/2

    print("Gross salary = %.0f" % gross_salary)
    print("Net income = %.0f" % net_income)
