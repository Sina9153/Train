with open("Test1.txt","w") as file:
    file.write("Ali=20")
with open("Test1.txt","r") as file:
    print(file.read())