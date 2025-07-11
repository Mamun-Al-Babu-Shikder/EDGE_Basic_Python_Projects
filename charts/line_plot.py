import matplotlib.pyplot as plt

years = [2019, 2020, 2021, 2022, 2023]
gpas = [2.8, 3.0, 3.2, 3.5, 3.7]

plt.plot(years, gpas, marker='o', linestyle='--', color='purple')
plt.title("Gaussian Process Regression")
plt.xlabel("Year")
plt.ylabel("Gaussian Process")
plt.grid(True)
plt.show()

"""
plt.plot(..) → line plot
marker='o' → shows dots
linestyle='--' → the line style of the plot
color='purple'='--' → the line color of the plot
title(..), xlabel(..), ylabel(..), grid(..) → for labeling and clarity
"""
