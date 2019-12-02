import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
 
 

bars1 = [0, 41, 21, 20, 20]
bars2 = [20, 0, 0, 20, 62]
bars3 = [81, 0, 0, 0, 20]

bars = np.add(bars1, bars2).tolist()
 

 

r = ['CAN','FIN','SUI','SWE','USA']
barWidth = 0.5
 

plt.bar(r, bars1, color='orange', edgecolor='white', width=barWidth, label='Bronze')

plt.bar(r, bars2, bottom=bars1, color='grey', edgecolor='white', width=barWidth, label='Silver')
 
plt.bar(r, bars3, bottom=bars, color='gold', edgecolor='white', width=barWidth, label='Gold')



plt.xlabel("Countries")
plt.ylabel("Medals")
plt.title("Medals Achieved by Women Compared between Countries since 1998")
plt.legend()
plt.show()

