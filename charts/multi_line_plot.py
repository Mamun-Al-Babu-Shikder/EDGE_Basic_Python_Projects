from matplotlib import pyplot as plt


years = [2019, 2020, 2021, 2022, 2023]

students_count_cse = [28, 30, 32, 35, 37]
students_count_ict = [26, 29, 33, 36, 36]

plt.plot(years, students_count_cse, label="CSE Dept", marker='o')
plt.plot(years, students_count_ict, label="ICT Dept", marker='s')

plt.title("Student Count Comparison")
plt.xlabel("Year")
plt.ylabel("Student Count")
plt.legend()
plt.grid(True)
plt.show()
