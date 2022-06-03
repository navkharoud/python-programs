#!/usr/bin/env python
# coding: utf-8

# In[50]:


import numpy as np
import math


# In[52]:


def is_triangle(x):
    i=0
    while i < 3:
        y = np.array([True,True,True])
        if x[0,i] > (x[1,i]+x[2,i]) or x[1,i] > (x[0,i]+x[2,i]) or x[2,i] > (x[1,i]+x[0,i]):
            y[i]= False
        else:
            y[i]= True
        
        i +=1        
    return y


# In[53]:


# Create a 3x3 array of uniformly distributed
# random values between 0 and 1
x=np.random.random((3,3))


# In[54]:


x


# In[55]:


is_triangle(x)


# In[ ]:




