# import numpy as np

# list1 =np.array([10,20,30,40,50])
# print(list1)
# print(list1.shape)

# list2 = np.array([[1,2],[3,4],[5,6]])
# print(list2)
# print(list2.shape)

# list3 = np.array([10,20,30,40] , dtype = float)
# print(list3)

# import numpy as np
# list19 = np.array([[10, 20, 30] ,
#                    [40, 50, 60] ,
#                    [70 ,80, 90]])
# for inner_list in list19:
#     print("-----")
#     for element in inner_list:
#         print(element)
# import numpy as np
# list21 =np.array([1,2,3,4,5])
# print(np.sum(list21))
# print(np.mean(list21))
# print(np.min(list21))
# print(np.max(list21))
# print(np.std(list21))


import numpy as np
# list_name=np.array([1,2])
# list_name2 = np.array([3, 4])
# print(np.vstack((list_name, list_name2)))

# list_name = np.array([1, 2, 3, 4, 5," "])
# new_list = np.split(list_name ,2)
# print(new_list[0])
# print(new_list[1])

# list_name = np.array([1, 2, 3])
# list_name2 =list_name.copy()
# list_name2[0] = 100
# print(list_name)
# print(list_name2)

# np.random.seed(0)
# print(np.random.rand(2,2))
# print(np.random.randint(1,10,(2,3)))

list_name = np.array([1, 3, 2])
print(np.sort(list_name))
print(np.argsort(list_name))
