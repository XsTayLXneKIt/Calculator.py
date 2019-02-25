Author = 'XsTayLXneKIt'

Num1 = int(input('First Number: '))
Num2 = int(input('Second Number: '))
IfNum3 = str(input('Do You need Third number?: '))
if IfNum3 == 'yes':
    Num3 = int(input('Third Number: '))
    Sign = int(input('''
    1 - Plus
    2 - Minus
    3 - Multiplication
    4 - Divide
    Your Sign: '''))
    if Sign == 1:
        print(Num1 + Num2 + Num3)
    if Sign == 2:
        print(Num1 - Num2 - Num3)
    if Sign == 3:
        print(Num1 * Num2 * Num3)
    if Sign == 4:
        print(Num1 / Num2 / Num3)
elif(IfNum3 == 'no'):
    Sign = int(input('''
    1 - Plus
    2 - Minus
    3 - Multiplication
    4 - Divide
    Your Sign: '''))
    if Sign == 1:
        print(Num1 + Num2)
    if Sign == 2:
        print(Num1 - Num2)
    if Sign == 3:
        print(Num1 * Num2)
    if Sign == 4:
        print(Num1 / Num2)
