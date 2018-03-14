# Handle Missing Data
from sklearn.preprocessing import Imputer

# Label Encoding
from sklearn.preprocessing import OneHotEncoder

# Feature Scaling
from sklearn.preprocessing import StandardScaler

# Train Test Split
from sklearn.model_selection import train_test_split

import pandas as pd
import numpy as np

dataset = pd.read_csv('Social_Network_Ads.csv')

X = dataset.iloc[:,1:4].values
y = dataset.iloc[:,-1].values

# Feature Scaling
sc = StandardScaler()
#X[:,2:4] = sc.fit(X[:,2:4])
X[:,2:4] = sc.fit_transform(X[:,2:4])

#print(X)
