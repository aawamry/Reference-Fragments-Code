__credits__ = "Ahmad Lotfy"
__author__ = ["Python Projects", "Laura Cassel", "Alan Gauld"]
__date__ = "04/29/2024"
__version__ = "1.0"
__email__ = "ahmadlotfy1021@gmail.com"

##----------------------------------------------------------------------------------------


target = int(66)

while True:
    value = input("Enter an integer between 1 and 100:\n")
    
    try:
        value = int(value)
    
    except ValueError:
        print("Wrong Value please enter an Integer!")
        continue
        break
    
    if value > target:
        print("\nIncorrect", value, "is too HIGH\n")
    elif value < target:
        print("\nIncorrect", value, "is too LOW\n")
    else:
        print("That's correct, please check the file")
        with open("tmp.txt", "w") as tmp:
            print("Hello", "World The value is: ", target, end= '\n-------End-------', sep=" ", file=tmp)
            
    print("do you need to repeat?\n if (Yes) enter: y\n if (No) enter: n\n")
    repeat = str(input())
    if repeat == "y":
        continue
    if repeat == "n":
        break
                
           
                
         