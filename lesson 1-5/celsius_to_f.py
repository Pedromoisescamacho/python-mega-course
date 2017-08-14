#a function to convert Celsius to Fahrenheit.
temperatures=[10,-20,-289,100]

with open("temperatures.txt","w") as file:
    for t in temperatures:
        if t > -275.15:
            f=t*9/5+32
            file.write(str(f)+ "\n")
