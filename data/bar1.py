import numpy as np
import matplotlib.pyplot as plt
 

height = [250, 101]
bars = ('Men', 'Women')
y_pos = np.arange(len(bars))
 

plt.barh(y_pos, height)
plt.yticks(y_pos, bars)
plt.xlabel("Total Medal Counts")
plt.title("Total Medal Counts of Canadian Men and Women in Ice Hockey since 1998")
plt.show()
