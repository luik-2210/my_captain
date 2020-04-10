#!/usr/bin/env python
# coding: utf-8

# In[3]:


import string
import random


# In[5]:


print('How many accounts you want to have?')
n=int(input())
for i in range(n):
    def uname(l):
        a=string.ascii_letters + string.digits
        return ''.join(random.choice(a) for i in range(l))
    def pword(l):
        b=string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(b) for i in range(l))
    def sname(l):
        return ''.join(random.choice(string.ascii_uppercase) for i in range(l))
    print("Length of Name = ")
    c=int(input())
    print(sname(c))
    print("Length of Username = ")
    d=int(input())
    print(uname(d))
    print("Length of Password = ")
    e=int(input())
    print(pword(e))


# In[ ]:




