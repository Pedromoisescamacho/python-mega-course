def login():
    password = ""
    while password != "password1":
        password = input("please enter your password: ")
        if password == "password1":
            print("access granted")
        else:
            print("please try again")

login()
