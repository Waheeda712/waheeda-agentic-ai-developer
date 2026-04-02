 # Without lambda function
# numbers =[1,2,3,4,5]
# def square(num):
#     return num*num
# result = map(square , numbers )
# print(list(result))

# With using lambda function

#print(list(map(lambda num : num * num ,[1,2,3,4,5])))

print(list(filter(lambda num1 : num1 % 2 == 0 ,[1,2,3,4,5])))