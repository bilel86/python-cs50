def main():
    x=input(" how are you !")
    convert(x)

def convert(x):
    j=0
    for i in x:
        
        if i == ":" and x[int(j+1)] ==")" :
            
            print('🙂', end='')
            break
        elif i == ":" and x[int(j+1)] =="(" :
            
             print('😢', end='') 
             break          
        else:
            print(i, end='')
        j+=1 
        continue
                 
main()
