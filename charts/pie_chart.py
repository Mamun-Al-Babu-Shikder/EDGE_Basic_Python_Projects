import matplotlib.pyplot as plt

departments = ['CSE', 'EEE', 'ICT', 'TE']
counts = [10, 8, 5, 17]

plt.pie(counts, labels=departments, autopct='%1.1f%%', startangle=90)
plt.title('Enrolled Counts')
plt.axis('equal')
plt.legend()
plt.show()

"""
autopct='%1.1f%%': Show % with 1 decimal
startangle=90: Rotates chart to start at 90°
axis('equal'): Keeps it circular
"""
