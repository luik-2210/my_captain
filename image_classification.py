#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#using pandas to read the database stored in the same folder
data = pd.read_csv('MNIST_data.csv')


# In[3]:


#viewing column heads
data.head()


# In[4]:


#extracting the data from the dataset and viewing them up close
a=data.iloc[3,:].values


# In[5]:


#reshaping the extracted data into a reasonable size
a=a.reshape((28,28)).astype('uint8')
plt.imshow(a)


# In[6]:


#seperating the labels and data values
DataY=pd.read_csv('MNIST_target.csv')
df_x=data.values
df_y=DataY.values


# In[7]:


#Creating Training and Testing Data
x_train,x_test,y_train,y_test=train_test_split(df_x,df_y,test_size=0.2,random_state=4)


# In[8]:


#Calling RF Classifier
rf=RandomForestClassifier(n_estimators=1000)


# In[9]:


#Fitting the model
rf.fit(x_train,y_train )


# In[10]:


pred=rf.predict(x_test)


# In[11]:


pred


# In[14]:


#calculate no.of correctly predicted values
count=0
for i in range(len(pred)):
    if(pred[i]==y_test[i]):
        count+=1


# In[15]:


count


# In[17]:


len(pred)


# In[18]:


print((count/len(pred)*100))


# In[ ]:




