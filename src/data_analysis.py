import pandas as pd

df = pd.read_csv("data/student_data.csv")

#print("\nDATASET INFO:")
#df.info()
#print(df.describe())
"""
#for selecting one column

#print("\nSTUDY HOURS:")
#print(df["study_hours"])
"""
"""
#for selecting multiple columns

print("\nSTUDY HOURS + ATTENDANCE:")
print(df[["study_hours", "attendance"]])
"""
"""
#Filtering = selecting only the rows that satisfy a condition.
print("\nSTUDENTS WITH MORE THAN 5 STUDY HOURS:")
print(df[df["study_hours"] > 5])

print(df[df["attendance"] >= 80])
"""
"""
#Multiple Conditions
#Now we combine two conditions.
#🎯 Task
#Find students who:
#studied more than 5 hours
#AND have attendance of at least 85%
print("\nSTUDENTS WITH >5 STUDY HOURS AND >=85% ATTENDANCE:")
print(df[(df["study_hours"] > 5) & (df["attendance"] >= 85)])
"""
"""
print("\nMEAN:")

print("Study Hours:", df["study_hours"].mean())
print("Attendance:", df["attendance"].mean())
print("Previous Score:", df["previous_score"].mean())
print("Final Score:", df["final_score"].mean())
"""
"""
print("\nMEDIAN:")

print("Study Hours:", df["study_hours"].median())
print("Final Score:", df["final_score"].median())
"""
"""
#CORRELATION
print("\nCORRELATION:")
print(df.corr(numeric_only=True))
"""
"""
#Sort the students by final_score from lowest → highest.
print(df.sort_values("final_score"))
#Sort final_score from highest → lowest.
print(df.sort_values("final_score", ascending=False))
"""

#print(df.isnull())
#print(df.isnull().sum())
"""
test_df = df.copy()
#Creates a separate copy of your dataset, so your original df stays safe.
test_df.loc[2, "study_hours"] = None
#Changes the study_hours value at row 2 to a missing value.
print(test_df)
print(test_df.isnull().sum())
"""
"""
print(df[df["study_hours"] > 5])
#Show only students whose study_hours are greater than 5.
print(df[df["final_score"] >= 80])
#Show students whose final_score is 80 or higher.
"""
"""
X = df[[
    "study_hours",
    "attendance",
    "previous_score",
    "assignments_completed",
    "sleep_hours"
]]

y = df["final_score"]

print("Features:")
print(X)

print("Target:")
print(y)
"""
"""
X = df[[
    "study_hours",
    "attendance",
    "previous_score"
]]
y = df["final_score"]
print("X:")
print(X)

print("\ny:")
print(y)
"""

import pandas as pd

df = pd.read_csv("data/student_data.csv")

print("HEAD:")
print(df.head())

print("\nSHAPE:")
print(df.shape)

print("\nINFO:")
df.info()

print("\nDESCRIBE:")
print(df.describe())

print("\nMISSING VALUES:")
print(df.isnull().sum())

print("\nSORTED BY FINAL SCORE:")
print(df.sort_values("final_score", ascending=False))

print("\nSTUDENTS WITH >= 4 STUDY HOURS:")
print(df[df["study_hours"] >= 4])

print("\n===== STUDENT ANALYSIS =====")

print("Number of students:", df.shape[0])

print("Average study hours:", df["study_hours"].mean())

print("Average attendance:", df["attendance"].mean())

print("Average previous marks:", df["previous_score"].mean())

print("Average final marks:", df["final_score"].mean())

print("Highest final marks:", df["final_score"].max())

print("Lowest final marks:", df["final_score"].min())

print("Students with >= 4 study hours:",
      (df["study_hours"] >= 4).sum())

print("Missing values:")
print(df.isnull().sum())