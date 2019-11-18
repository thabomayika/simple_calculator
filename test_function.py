
##addition
def add(num1, num2):
    return num1+num2

##muliply
def multiply(num1, num2):
    return num1*num2

print("choose operations") 
print('1. Add')
print('2. Multiply') 

choose = input('Enter operations: ')
num1 = float(input('Enter a number: '))
num2 = float(input('Enter another number: '))

if choose == "1" :
    print(add(num1,num2))
elif choose == "2" :
    print(multiply(num1,num2))
else:
    print("invalid value")    


