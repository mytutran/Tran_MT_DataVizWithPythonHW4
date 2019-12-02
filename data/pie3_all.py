import numpy as np
import matplotlib.pyplot as plt



labels = ["USA", "SWE", "SUI", "FIN", "CAN"]
sizes = [102, 40, 21, 41, 101]
colors = ['green', 'teal', 'red', 'orange', 'blue']



plt.pie(sizes, colors=colors, labels=labels, shadow=True, startangle=90, autopct='%1.1f%%')
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Total Medals Counts of Canadian Women Compared To Other Countries")
plt.xlabel("Medal Counts since 1998")
plt.show()