username = input("Please enter your username: ")
password = input("Please enter your password: ")
if username == "sean" and password == "156545":
    print("Access Granted")
else:
    if username != "sean":
        print("Username incorrect")
    if password != "156545":
        print("Password incorrect")
