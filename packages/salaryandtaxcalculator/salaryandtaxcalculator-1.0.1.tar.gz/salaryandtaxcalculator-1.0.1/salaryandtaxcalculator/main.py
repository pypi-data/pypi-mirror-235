def salary_calculator():
    salary = int(input('Enter salary: '))

    if salary < 400:
        tax = 0
        print('Tax is in the first range, tax is 0%.')
    elif 400 <= salary <= 1500:
        tax = salary * 0.13
        print(f'The tax is {tax}.')
    elif salary > 1500:
        tax = salary * 0.23
        print(f'The tax is {tax}.')
    else:
        salary = 0
        print('ERROR: Salary cannot be negative.')


salary_calculator()

