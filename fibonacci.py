#!/usr/bin/env python
# coding: utf-8

# In[14]:


n=int(input("Enter the number = "))
a,b=0,1
for i in range(n):
    if i==0 or i==1:
        print(i)
    else:
        c=a+b
        print(c)
        a=b
        b=c


# In[ ]:




