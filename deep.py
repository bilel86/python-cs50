x=input("...")

if x.strip()=='42':
    print("yes") 
elif x.lower().strip()== "forty-two":
    print("yes")
elif x.lower().strip()=="forty two":
    print("yes")
else:
    print("no")
