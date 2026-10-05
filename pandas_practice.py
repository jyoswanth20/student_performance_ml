"""import pandas as pd

data = {
    "Name": ["Ravi", "Anu", "Kiran", "Priya"],
    "Age": [20, 21, 20, 22],
    "Marks": [85, 92, 76, 88]
}

df = pd.DataFrame(data)

print("Full DataFrame:")
print(df)

print("\nNames:")
print(df["Name"])

print("\nMarks:")
print(df["Marks"])

print("\nName and Marks:")
print(df[["Name", "Marks"]])
"""

import pandas as pd

data = {
    "Name": ["Ravi", "Anu", "Kiran", "Priya", "Arjun"],
    "Age": [20, 21, 20, 22, 21],
    "Marks": [85, 92, 76, 88, 95]
}
df = pd.DataFrame(data)
#print(df.head())
#print(df.tail())
#print(df.shape)
#print(df.columns)
#print(df.info())
#print(df.describe())
#print("\n3. SHAPE:")
#print(df.shape)
print("\n4. COLUMNS:")
print(df.columns)