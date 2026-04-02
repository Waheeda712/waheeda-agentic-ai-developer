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

drop_row_based_age_salary = db.dropna(subset=["age","Salary"])
print(drop_row_based_age_salary)