#RECURRSION
#  def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)
# res = factorial(5)
# print(res)


# LAMBDA function
#Ex:
# res = lambda num1 : num1*num1 
# print(res(6))
# x = res(4)
# print(x)

#Ex:
# result = lambda num1 , num2 : num1 + num2
# print( result (100, 200))

#Nested functions
# def outer():
#     def inner():
#         print("Hello world")
#     inner()

# outer()

# def outer(num1):
#     def inner(num2):
#         return num1 + num2
#     return inner

# x = outer(100)
# res = x(200)
# print(res)

#Global Variables & Local Variables

# x = 10 # global variable
# def test_func():
#     x = 20 # Local variable
#     print(x)
# test_func() # this will return local variable
# print(x) # this will return global variable

# GLOBAL VARIABLE USED INSIDE THE FUNCTION
# x = 20
# def test_func():
#     global x
#     x = 30
#     print(x)
# test_func()
# print(x)

x =10
def outer():
    def inner():
        global x
        x = 20
        print(x)

        def innerin():
            global x
            x = 40

            print(x)
        innerin()
    inner()
outer()

