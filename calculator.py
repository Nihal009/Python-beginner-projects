def addition():
    a=int(input('Enter a Number:'))
    b=int(input('Enter another Number:'))
    return a+b


def subtraction():
    a=int(input('Enter a Number:'))
    b=int(input('Enter another Number:'))
    return a-b


def multiplication():
    a=int(input('Enter a Number:'))
    b=int(input('Enter another Number:'))
    return a*b
    

def division():
    a=int(input('Enter a Number:'))
    b=int(input('Enter another Number:'))
    return a/b


print('--------------------Calculator------------------------------')
ch=0
while ch!=5:
    print('\n\nOperations:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit\n')
    ch=int(input('enter a choice: '))
    if ch==1:
        print(addition())
    elif ch==2:
        print(subtraction())
    elif ch==3:
        print(multiplication())
    elif ch==4:
        print(division())
    else:
        break

