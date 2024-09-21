try:
    a=int(input('Enter a: '))
    b=int(input('Enter b: '))
    c=a/b
    print('Number is: ',c)
except ValueError as v:
    print('Error is:',v)
except ZeroDivisionError as z:
    print('Error is:',z)
except SyntaxError as s:
    print('Error is:',s)
else:
    print('Successful')
finally:
    print('Program ended')