# Handle Missing Data
from sklearn.preprocessing import Imputer

# Label Encoding
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# Feature Scaling
from sklearn.preprocessing import StandardScaler

# Train Test Split
from sklearn.model_selection import train_test_split

import pandas as pd
import numpy as np

dataset = pd.read_csv('Data.csv')

X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

print(X)

# Handle Missing Data
imputer = Imputer(missing_values='NaN', strategy='mean')
X[:,1:3] = imputer.fit_transform(X[:,1:3])
print(X)

label = LabelEncoder()
X[:,0] = label.fit_transform(X[:,0])
print(X)

oneHot = OneHotEncoder(categorical_features=[0])
X = oneHot.fit_transform(X).toarray()

# Feature Scaling
sc = StandardScaler()
#X[:,2:4] = sc.fit(X[:,2:4])
X[:,3:5] = sc.fit_transform(X[:,3:5])

#print(X)


# Train Test Split
X_train,x_test,y_train, y_test = train_test_split(X,y,test_size=0.2)

