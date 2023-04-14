def main():
    time=input("what time is it?").replace(":",".")
    
    print(convert(time))

def convert(time):
    if float(time)>=7.0 and float(time)<=8.0:
        return "breakfast time"
    if float(time)>=12.0 and float(time)<=13.0:
        return "lunch time"
    if float(time)>=18.0 and float(time)<=19.0:
        return "dinner time"


if __name__ == "__main__":
    main()
