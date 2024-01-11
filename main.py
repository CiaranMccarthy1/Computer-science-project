#.venv\Scripts\activate

# IMPORTS

# numpy
# matplotlib
# scipy

########################

# FLOW

# 1) embedded systems

# 2) python 
#   -data in csv file 
#   -LCH statictics 

# 3) produce graphs
# 4) Gui
# 5) video 
# 6) store data 

# 7) Report 
#   -index.html 

########################

# TIMELINE

# Jan 5th 
# Jan 15th (2,3,6)
# Jan 20th (7)

from random import choice
from turtle import color
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Start")
     
# open files
data = pd.read_csv("Data.csv")
Heartrate = np.array(data) # have to turn pandas variabe into np array 



# Anaylise data
average = np.nanmean(Heartrate)

# plot graph
plt.plot(Heartrate)
plt.axhline(y=np.nanmean(Heartrate), color = "red", linewidth=3)


# print data
print(np.nanmean(Heartrate))
plt.show()