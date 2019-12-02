import numpy as np
import matplotlib.pyplot as plt



labels = ["Gold"]
sizes = [71]
colors = ['yellow']



plt.pie(sizes, colors=colors, labels=labels, shadow=True, startangle=90, autopct='%1.1f%%')
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Medals Achieved by Canadian Men in Ice Hockey")
plt.xlabel("Medal Counts Since 1998")
plt.show()