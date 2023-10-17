def salary_tax(salary):
    if salary <= 400:
        print('TAX 0')
    elif salary >= 400 <=1500:
        tax = salary * 0.13
        print(f"{tax}")
    else:
        tax = salary * 0.23
        print(f"{tax}")

salary_tax(1900)


