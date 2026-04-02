import pandas as pd
db = pd.read_csv("employee.csv")
print(db)
print("---------------------")
# print(db.isnull())
# print("------------------------")
# print(db.notnull())
# print("-----------------------")
# print(db.isnull().sum())

# print(db.dropna())
# print("-----------------------")
# print(db.dropna(how="all"))

# drop_row_based_on_age = db.dropna(subset=["age"])
# print(drop_row_based_on_age)
# print("-----------------------")
# drop_row_based_on_salary = db.dropna(subset=["Salary"])
# print(drop_row_based_on_salary)
# print("-----------------------")

# drop_row_based_age_salary = db.dropna(subset=["age","Salary"])
# print(drop_row_based_age_salary)
# print("-----------------------")

# fill_with_zero=db.fillna(0)
# print(fill_with_zero)

#db["age"] = 20 # print all the age with 20
# db["age"] = db["age"].fillna(db["age"].mean()) # print the empty age with mean vaule
# db["Salary"] = db["Salary"].fillna(db["Salary"].mean())
# print(db)

forward_fill = db.ffill()
print(forward_fill) # fill the empty vaules with forward value
print("-----------------------")
backward_fill = db.bfill()
print(backward_fill) # fill the empty values with backwardvaule