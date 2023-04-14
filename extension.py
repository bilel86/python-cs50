def main():
    
    list=input("what's your file to need download\n").lstrip()
    listt=list.lower().split('.')
    
    extension(listt)

def extension(listt):
    if listt[len(listt)-1] == "gif":
        return print("image/"+listt[len(listt)-1])
    elif listt[len(listt)-1] == "pdf":
        return print("image/"+listt[len(listt)-1])
    elif listt[len(listt)-1] == "jpeg" or listt[len(listt)-1] == "jpg" :
        return print("image/"+listt[len(listt)-1])
    elif listt[len(listt)-1] == "png":
        return print("image/"+listt[len(listt)-1])
    elif listt[len(listt)-1] == "txt":
        return print("image/"+listt[len(listt)-1])
    elif listt[len(listt)-1] == "zip":
        return print("image/"+listt[len(listt)-1])
    else:
        return print("app")


main()
