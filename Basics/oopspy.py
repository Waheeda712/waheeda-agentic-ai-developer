# class Student:
#     pass
# s1=Student()
# print(type(s1))

# class Student:
#     def __init__(self):
#         print("Constructor")
# s1 = Student()


# class Student:
#     def __init__(self , name , age):
#         self.name = name
#         self.age = age
# s1=Student("Waheeda", "20")
# print(s1.name , s1.age)

# class Student:
#     def __init__(self , name , age , marks, grade):
#         self.name = name
#         self.age = age
#         self.marks = marks
#         self.grade = grade
#     def display(self):
#         print(self.name , self.age ,self.marks, self.grade)

# s1 = Student("Waheeda", "20", 90 , "A")
# s1.display()

class Student:
    msg = "Hello World"
    def __init__(self , name):
        self.name = name
s1 = Student("Waheeda")
print(s1.name ,s1.msg)
        