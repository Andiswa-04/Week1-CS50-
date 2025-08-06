user_expression = input("Expression:")
x,y,z = user_expression.split(" ")

x,z = float(x) , float(z)

if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    print(x / z)
else:
    print("Perhaps try an expression with only 2 values")



