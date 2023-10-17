def tax(x):
    if 0 <= x <= 400:
        print('Tax = 0')
    elif 400 < x < 1500:
        print(f'Tax = {0.13 * x}')
    elif 1500 <= x:
        print(f'Tax = {0.23 * x}')


tax(550)
