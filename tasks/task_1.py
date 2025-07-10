"""
1. Create a students.csv file with at least 5 records (realistic or dummy data).
2. Load it in Python using pandas.
3. Do the following:
    3.1 Print first 3 rows
    3.2 Show the average GPA
    3.3 Filter and print students from CS department
    3.4 Show only students who are enrolled and have GPA > 3.0
"""

import pandas as pd

# Load students.csv using pandas
df = pd.read_csv("students.csv")

# Print first 3 rows
print(df.head(3))

# Show the average GPA
print(f"\nAverage GPA: {df['GPA'].mean()}", end='\n\n')

# Filter and print students from CS department
cs_students = df[df['Department'] == 'CS']
print(cs_students, end='\n\n')

# Show only students who are enrolled and have GPA > 3.0
enrolled_with_gpa = df.query('Enrolled == "Yes" & GPA > 3.0')
print(enrolled_with_gpa)
