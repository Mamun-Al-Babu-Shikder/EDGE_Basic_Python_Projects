from matplotlib import pyplot as plt

gpas = [2.5, 2.8, 3.0, 3.4, 3.5, 3.6, 3.2, 2.9, 3.8, 3.1]

plt.hist(gpas, bins=5, color='pink', edgecolor='black')
plt.title("GPA Distribution")
plt.xlabel("GPA")
plt.ylabel("Number of Students")
plt.show()

