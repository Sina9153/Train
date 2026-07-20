abc = input("What do you want? \npassword checker,text analyzer or phone checker")

if "password checker" in abc:
 password = input("Enter password: ")

 special = "!@#$%^&*()_-+=<>?/"

 has_number = False
 has_upper = False
 has_special = False

 for i in password:
    if i.isdigit():
        has_number = True

    if i.isupper():
        has_upper = True

    if i in special:
        has_special = True

 if len(password) < 8:
    print("Error: Password must be at least 8 characters.")

 elif not has_number:
    print("Error: Password must contain a number.")

 elif not has_upper:
    print("Error: Password must contain an uppercase letter.")

 elif not has_special:
    print("Error: Password must contain a special character.")

 else:
    print("Your password is strong.")
elif "phone checker" in abc:
 phone = input("Enter phone number: ")

 phone = phone.replace(" ", "")
 phone = phone.replace("-", "")

 if phone.startswith("+98"):
    print("Phone number is correct.")
    print(phone)
 else:
    print("Error: Phone number must start with +98")
elif "text analyzer" in abc:
 text = input("Enter text: ")

 words = len(text.split())

 sentences = 0
 uppercase = 0
 lowercase = 0
 spaces = 0
 numbers = 0

 for i in text:

    if i in ".!?":
        sentences += 1

    if i.isupper():
        uppercase += 1

    if i.islower():
        lowercase += 1

    if i == " ":
        spaces += 1

    if i.isdigit():
        numbers += 1

 characters = len(text)

 print("Words:", words)
 print("Sentences:", sentences)
 print("Uppercase:", uppercase)
 print("Lowercase:", lowercase)
 print("Spaces:", spaces)
 print("Numbers:", numbers)
 print("Characters:", characters)

else:
    print("Program not found.")
