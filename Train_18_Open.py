with open("Test.txt","w") as my_file:
    my_file.write("Hello Word")
    my_file.close()

with open("Text.txt","r") as my_file:
    files_text=my_file.read()
print(files_text)

with open("Photos","rb") as file:
    image=file.read()
    print(image)

new_image=image[0:5000]

with open("Photos","wb") as file:
    file.write(new_image)