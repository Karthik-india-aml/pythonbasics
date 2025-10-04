num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))

operator=input("Give operator: ")

if operator == "+":
    print(f"Addition of 2 numbers is {num1+num2}")
elif operator == "-":
    print(f"Subtraction of 2 numbers is {num1-num2}")
elif operator == "*":
    print(f"Multiplication of 2 numbers is {num1*num2}")        
elif operator == "/":
    print(f"Division of 2 numbers is {num1/num2}")      

else:
    print("No operator")    