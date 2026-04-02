import pandas as pd

db = pd.read_csv("Book1.csv")
# print(db.tail())
# print(db.info())
# print(db.describe())
print(db)
# print(db.shape)
# print(db.columns)
# print(db.dtypes)

# print(db["Name"])
# print(db[["Name", "Age"]])
# print("------------------------")
# print(db.iloc[0]) #by index
# print("------------------------")
# print(db.loc[0]) # ny label
print(db[db["Age"]>30 and db["Salary"]>70000])