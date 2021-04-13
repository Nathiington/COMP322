num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

if num1 > num2:
    print('{0} is greater than {1}'.format(num1,num2))
if num2 > num1:
    print('{0} is greater than {1}'.format(num2, num1))
else:
    print('Both numbers are equal')
