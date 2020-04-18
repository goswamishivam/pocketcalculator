#Exercise: Pocket calculator


c=0
l=[]

def add(to_add):
    to_add=int(input("Enter the number which you want to add:"))
    global c
    c=to_add+c
    display_current_value()

def mult(to_mult):
    to_mult=int(input("Enter the number which you want to multiply:"))
    global c
    c=to_mult*c
    display_current_value()

def div(to_div):
    global c
    to_div=int(input("Enter the number which you want to divide:"))
    try: 
        c=c/to_div
        display_current_value()
    except Exception as e:
        print("Invalid input:",e)
       

def display_current_value():
    global c
    print("Current value:",c)
    l.append(c)


def undo():
    l.pop()
    l1=l[-1:]
    for i in l1:
        print("Current value after undo:",i)

def recall():
    global c
    print("Recalled value:",c)

def main():
    add(1)
    mult(1)
    div(1)
    recall()
    undo()
    
       

if __name__=="__main__":
    print("Welcome to the calculator program.")
    print("Current value:",c)
    main()
    


    
    
    
    
    
    
