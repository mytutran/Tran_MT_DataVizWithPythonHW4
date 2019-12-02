import numpy as np
import matplotlib.pyplot as plt



labels = ["Gold", "Silver"]
sizes = [81, 20]
colors = ['yellow', 'grey']



plt.pie(sizes, colors=colors, labels=labels, shadow=True, startangle=90, autopct='%1.1f%%')
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Medals Achieved by Canadian Women in Ice Hockey")
plt.xlabel("Medal Counts Since 1998")
plt.show()