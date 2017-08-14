#this is the way that we integrate user input into a function
#creating the function
def age_plus_50():
    while True:
        try:
            age = int(input("please enter a age: "))
            if 0 < age <= 150:
                print(age + 50)
                break
            else:
                print("please enter a realistic age, i.e. more than 0 and equal or below 150")

        except:
            print("please enter an integer")
            continue

age_plus_50()
