#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from joblib import dump, load
import xgboost as xgb
import numpy as np


# In[2]:


train_data = pd.read_csv('train.csv')


# In[3]:


train_data = train_data.fillna(0)


# In[4]:


train_data = train_data.dropna(how='all')


# In[5]:


scaler = MinMaxScaler()


# In[6]:


X = train_data.iloc[:,0:6]
y = train_data.iloc[:,6]


# In[7]:


#y_encoded = pd.get_dummies(y,prefix_sep='_')


# In[8]:


scaledDataArray = scaler.fit_transform(X.drop(['Timestamp'],axis=1))


# In[9]:


scaledDataArray


# In[10]:


scaledData = pd.DataFrame(scaledDataArray)


# In[11]:


seed = 7
test_size = 0.33
X_train, X_test, y_train, y_test = train_test_split(scaledData, y, test_size=test_size, random_state=seed)


# In[37]:


model = XGBClassifier(max_depth=3, n_estimators=300, learning_rate=0.05)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))
dump(model,'model.joblib')


# In[38]:


def process(df):
    scaledDataFrame = scaler.fit_transform(df.drop(['Timestamp'],axis=1))
    scaledData = pd.DataFrame(scaledDataArray)
    loaded_model = load(model.joblib)
    pred = loaded_model.predict(scaledData)
    return pred


# In[ ]:




