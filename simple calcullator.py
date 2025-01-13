#Simple Calculator

#Init
#Functions
def add(num1,num2):
    result=num1+num2
    print(result)
def sub(num3,num4):
    result=num3-num4
    print(result)
def mult(int5,int6):
    result=int5*int6
    print(result)
def div(int7,int8):
    result=int7/int8
    print(result)


print("Welcome to simple calculator")
while True:
    print("Please select an operation: ")
    print("""1. Add
    2. subtract
    3.Multiply
    4.Divide
    5.Quit""")
    operation = int(input("(1-5)Option:"))
    if operation == 1:
        int1= int(input("Enter the first number:"))
        int2= int(input("Enter the second number:"))
        add(int1,int2)
    elif operation == 2:
        num3= int(input("Enter the first number:"))
        num4= int(input("Enter the second number:"))
        sub(num3,num4)
    elif operation == 3:
        int5= int(input("Enter the first number:"))
        int6= int(input("Enter the second number:"))
        mult(int5,int6)
    elif operation == 4:
        int7= int(input("Enter the first number:"))
        int8= int(input("Enter the second number:"))
        div(int7,int8)
    elif operation ==5:
        break



#Main


