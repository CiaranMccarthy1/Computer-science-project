#.venv\Scripts\activate

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = np.array(pd.read_csv("Data.csv"))
sorteddata = np.argsort(data, axis = 0)

Stillrunning = True
while Stillrunning:
       Userchoice = input("Select on option \n1. Veiw raw data \n2. Veiw sorted data \n3. Veiw standard diviation \nPress 4 to exit\n")
       if Userchoice == "1":
           print(data)
           plt.plot(data)
           plt.show()
       if Userchoice == "2": 
           print (sorteddata)
           plt.plot(sorteddata)
           plt.show()
       if Userchoice == "3": 
           print(np.std(sorteddata))
       if Userchoice == "4":
           os.system("cls") 
           break
       

        