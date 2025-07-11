import matplotlib.pyplot as plt

departments = ['CSE', 'EEE', 'ICT', 'TE', 'BBA']
students_count = [30, 55, 20, 40, 65]

plt.bar(
    departments,
    students_count,
    color='green',
    align='center',
    edgecolor='gray',
    linewidth=2
)
plt.title("Students per Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.show()
