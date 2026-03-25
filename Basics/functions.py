#syntax of  function
# def class_name(): # defining funtion
#     print("Well come to python functions topic")

# class_name() #function call

#METHODS
#without parameters , without return type
# def login_user():
#     user_name = "waheeda"
#     password  = "Waheeda@123"
#     if(user_name == "waheeda" and password == "Waheeda@123"):
#         print("Login Successfully")
#     else:
#         print("Login Failed")
# login_user()


#without parameters , with return type
# def db_user():
#     user_name = "waheeda"
#     password  = "Waheeda@123"
#     if(user_name == "waheeda" and password == "Waheeda@123"):
#         return "Login successfully"
#     else:
#         return "Login Failed"
# result=db_user()
# print(result)

#with parameters , without return type
# def db_user(name , password):
     
#     if (name == "Waheeda" and password == "Waheeda@123"):
#         print("Login sucessful")
#     else:
#         print("Login Failed")
# db_user("Waheeda" , "Waheeda@123")

#with parameters , with return type
# def db_user(name , password):
     
#     if (name == "Waheeda" and password == "Waheeda@123"):
#        return "Login Successful"
#     else:
#         return "Login Failed"
# result=db_user("Waheeda" , "Waheeda@123")
# print(result)  


#default Parameter
# def db_user(name = "Katike", password = "Waheeda@123"):
#     if(name == "Waheeda" and password == "Waheeda@123"):
#         print (name, "Login successfully")
#     else:
#         print( name, "login failed")
# db_user("Waheeda", "Waheeda@127")

#Keywork Argument
# def test_func(name, age):
#     print(name, age)
# test_func(age=20, name="waheeda")
# test_func(name="ruhaan", age=25)


#Arbitrary argumnets

def  test_func(*num):
    print(sum(num))
    print(len(num))
    print(max(num))
    print(min(num))

test_func(10, 20, 30, 40, 50)
def test_fun(*name):
    print(name)

test_fun("Waheeda", "Ruhaan", "Mehar", "Arhaan")