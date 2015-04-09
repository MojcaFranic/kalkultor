a = raw_input("Povej 1. stevilko")
print(a)
b = raw_input("Povej 2. stevilko")
print(b)
operacija = raw_input("izbrei operacijo; +, -, /, *")
print(operacija)

a = float(a)
b = float(b)

if operacija == "+":
    print(a + b)
elif operacija == "-":
    print(a - b)
elif operacija == "/":
    print (a / b)
elif operacija == "*":
    print (a * b)
else:
    print("neznana operacija")

