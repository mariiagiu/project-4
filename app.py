import numpy as np
import pandas as pd 

data = {'Year' : [i for i in range(100)],
        'Age' : [i for i in range (100,200)],
        'Numbers' : [i for i in range (1000,1100)]}

df = pd.DataFrame(data)
df.to_csv('data.csv')