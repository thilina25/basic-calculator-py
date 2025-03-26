unit = input("Enter (C)elsius or (F)ahrenheit: ")
temp = float(input("Enter the temperature: "))
if unit == 'C':
    temp = round((temp * 9/5) + 32, 1)
    unit = '°F'
    print(f'Temperature is {temp} {unit}')
elif unit == 'F':
    temp = round((temp - 32) * 5/9, 1)
    unit = '°C'
    print(f'Temperature is {temp} {unit}')
else:
    print('Invalid input')
