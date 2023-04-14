def main():
    x, y, z=input("entrer un atithmetic expression").split(" ")
    print(f"{calculate(x,y,z):.1f}")

def calculate(x,y,z):
    if y =="+":
        result = float(x) + float(z)
        return result
    elif y == "-":
        result = float(x) - float(z)
        return result
    elif y == "*":
        result = float(x) * float(z)
        return result
    elif y== "/":
        result = float(x) / float(z)
        return result


main()
