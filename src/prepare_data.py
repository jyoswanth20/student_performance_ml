"""
import pandas as pd

df = pd.read_csv("data/student_data.csv")

print(df)
"""

import pandas as pd

df = pd.read_csv("data/student_data.csv")

X = df[[
    "study_hours",
    "attendance",
    "previous_score"
]]

y = df["final_score"]

print("Features (X):")
print(X)

print("\nTarget (y):")
print(y)

print("\nX shape:", X.shape)
print("y shape:", y.shape)

print("\nFeature statistics:")
print(X.describe())

print("\nMissing values:")
print(X.isnull().sum())

print("\nTarget statistics:")
print(y.describe())

print("\nX columns:", X.columns.tolist())
print("\nY column:", y.name)