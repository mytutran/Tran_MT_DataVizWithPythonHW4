import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 

Men = [0, 23, 23, 23, 25]
Women = [20, 20, 19, 21, 21]
Year = [1998, 2002, 2006, 2010, 2014]


plt.plot(Year, Women, color='pink', label='Women')
plt.plot(Year, Men, color='blue', label='Men')



plt.title("Medals Count Comparison between Canadian Men and Women")
plt.ylabel("Medal Counts Since 1998")
plt.xlabel("Year")
plt.legend()
plt.show()