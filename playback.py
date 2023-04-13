x=input("what is this\n")
print(x)

for i in x:
    if i == " ":
        print("...", end='')
    else:
        print(i, end='')
