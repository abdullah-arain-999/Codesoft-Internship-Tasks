print(('------------------------------------'))
print(('          <--CALCULATOR-->          '))
print(('------------------------------------'))


def calculation():
    a = int(input('Enter First Number : '))
    b = int(input('Enter Second Number :'))

    print("Choose the operation you want to perform:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Remainder (%)")
    userinput = input("Enter the operation (+, -, *, /,%): ")
    if(userinput=='+'):
        add=a+b
        j=f'ADDITION OF {a} AND {b} IS : {add}'
        print(j)
    elif (userinput == '-'):
        sub = a - b
        j = f'SUBTRACTION OF {a} AND {b} IS : {sub}'
        print(j)
    elif (userinput == '*'):
        mul = a * b
        j = f'MULTIPLICATION OF {a} AND {b} IS : {mul}'
        print(j)
    elif (userinput == '/'):
        if(a!=0 or b!=0):
            div = a / b
            j = f'DIVISION OF {a} AND {b} IS : {div}'
            print(j)
        else:
            print('PLEASE ENTER VALID INPUT !')

    elif (userinput == '%'):
        rem = a % b
        j = f'REMAINDER OF {a} AND {b} IS : {rem}'
        print(j)

calculation()
while True:
    wloop=input('\nIF YOU WANT TO DO AGAIN PRESS "A" FOR AGAIN OR "E" FOR EXIT : ')
    if(wloop=='A'.lower()):
        calculation()
    elif(wloop=='E'.lower()):
        break
    else:
        print('ENTER VALID INPUT')


print('Thanks for visiting ')