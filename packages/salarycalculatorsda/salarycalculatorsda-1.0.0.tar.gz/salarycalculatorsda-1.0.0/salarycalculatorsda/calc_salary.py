def salary_calc(x=0):
    if x <= 400:
        print(f"Salary is {x}$.")
    elif x > 400 and x <= 1500:
        a = x * 0.13
        b = x - a
        print(f"Salary is {b}$ | Tax is {a}$")
    else:
        a = x * 0.13
        b = x - a
        print(f"Salary is {b} | Tax is {a}$.")


salary_calc(x=1200)
