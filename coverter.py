weight = float(input("Enter your weight: "))
unit = input("Enter (L)bs or (K)g: ")
if unit == 'L':
    weight = weight / 2.205
    unit = 'Kg'
    print(f'You are {weight} kilos {unit}')
elif unit == 'K':
    weight = weight * 2.205
    unit = 'Lbs'
    print(f'You are {weight} pounds {unit}')
else:
    print('Invalid input')
