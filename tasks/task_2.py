"""
1. Create a students_dirty.csv file with:
    a. At least 1 missing age
    b. At least 1 missing GPA
    c. At least 1 duplicate row

2. Write Python code to:
    a. Detect and print missing values count
    b. Remove duplicate rows
    c. Fill missing GPA with 0
    d. Fill missing Age with average age
"""

import pandas as pd

df = pd.read_csv('students_dirty.csv')

# Detect and print missing values count
print("Missing values:\n", df.isnull().sum(), end='\n\n')

# Remove duplicate rows
df.drop_duplicates(inplace=True)
print("Without duplicate rows:\n", df, end='\n\n')

# Fill missing GPA with 0
df['GPA'].fillna(0, inplace=True)
print("Filled missing GPA with 0:\n", df, end='\n\n')

# Fill missing Age with average age
avg_age = int(df['Age'].mean())
df['Age'].fillna(avg_age, inplace=True)
print("Filled missing Age with average age:\n", df)
