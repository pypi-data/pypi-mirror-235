def salary_calculator(x):
    if x > 0 and x <= 400:
        print(f'neto payment {x}')
    elif x > 400 and x < 1500:
        tax = x * 0.13
        print(f'tax : {tax}')
    elif x > 1500:
        tax = x * 0.23
        print(f'tax : {tax}')
    else:
        print('Wrong number')

salary_calculator(9000)

