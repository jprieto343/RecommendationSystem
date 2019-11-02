# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 17:05:43 2019

@author: Josue Prieto
"""

import pandas as pd
import numpy as np
import seaborn as sns
df = pd.read_csv('ratings_Beauty.csv')


stat = df.describe()
rate = df['Rating']

sns.distplot(rate)


prod_rate = df.groupby('ProductId').mean()#.agg(avg_rate=('Rating', np.mean),stdev_rate=('Rating', np.std) )