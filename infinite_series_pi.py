#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import math


# In[7]:


def numeric():
    num = 2 * math.sqrt(2) / 9801
    return num


# In[8]:


def factorial(x):
    """Computes factorial of n recursively."""
    """if the value of x is 0 then it will return 1"""
    """because zero factorial is 1"""
    if x == 0:
        return 1
    else:
        """ factor is basically causing recurssion"""
        factor = factorial(x-1)
        result = x * factor
        return result


# In[15]:


def calcPi(k):
    i=0
    array=np.random.random(k)
    while i<k:
        """numenator will do upper part of calculation"""
        numenator = factorial(4*i) * (1103 + 26390*i)
        """denominator will do lower part of calculation"""
        denomenator = factorial(i)**4 * 396**(4*i)
        """term will provide one solution of equation"""
        term = numeric() * numenator / denomenator
        array[i]=term
        i +=1
    return 1/array.sum()


# In[16]:


x=calcPi(20)
x


# In[ ]:




