student={}
student["name"]=input("enter your first name:")
student["age"]=input("enter your age:")
student["final score"]=input("enter your final score:")
a=input("what do what do you want to now about yourself?")
if "name" in a:
    print("your name is",student["name"])
    if "age" in a:
     print("you are",student["age"],"years old")
    elif "final score" in a:
     print("your final score is",student["final score"])
    else:
       print("OK")

elif "age" in a:
    print("you are",student["age"],"years old")
    if "name" in a:
       print("your name is",student["name"])
    elif "final score" in a:
     print("your final score is",student["final score"])
    else:
       print("OK")

elif "final score" in a:
    print("your final score is",student["final score"])
    if "age" in a:
     print("you are",student["age"],"years old")
    elif "name" in a:
       print("your name is",student["name"])
    else:
       print("OK")
else:
   print("OK")
