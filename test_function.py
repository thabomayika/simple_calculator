


##addition
def add(*n):
    add = 0
    for num in n:
        add += num

    return add

##muliply
def multiply(*b):
    multiply = 1 
    for num in b:
        multiply *= num

    return multiply

print(" choose operations") 
print('1. Add')
print('2. Multiply') 

choose = input('Enter operations: ')
num1 = float(input('Enter a number: '))
num2 = float(input('Enter another number: '))

if choose == "1" :
    print(add(num1+num2))
elif choose == "2" :
    print(multiply(num1*num2))
else:
    print("invalid value")
