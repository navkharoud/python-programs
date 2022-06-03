#!/usr/bin/env python
# coding: utf-8

# In[140]:


import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import timeit
import random
import sys


# In[141]:


start_time = timeit.default_timer()
figure, axes = plt.subplots()
draw_circle = plt.Circle((0, 0), 1, fill=False)

axes.set_aspect(1)
axes.add_artist(draw_circle)
plt.show()


# In[142]:


MAX_X_VALUES = 200


# In[143]:


a, b = [np.random.random(MAX_X_VALUES) for _ in range(2)]


# In[144]:



figure, axes = plt.subplots()
draw_circle = plt.Circle((0, 0), 1,fill=False)

axes.set_aspect(1)
axes.add_artist(draw_circle)
axes.add_artist(plt.scatter(x=a, y=b ,))
plt.show()


# In[145]:


fx = a ** 2 + b ** 2 < 1
fx


# In[146]:


print((fx.sum()/200)*4 )
time_1 = timeit.default_timer() - start_time


# In[147]:


start_time = timeit.default_timer()
def mc_pi():
    inside_unit_circle = total_points = 0
    while True:
        total_points += 1
        a, b = random.random(), random.random()
        if a ** 2 + b ** 2 < 1:
            inside_unit_circle += 1
        yield 4 * inside_unit_circle / total_points


def main(max_iterations=200):
    for i, pi in enumerate(mc_pi()):
        if i > max_iterations:
            break
    print(pi)


if __name__ == '__main__':
    main(int(sys.argv[1]))
time_2 = timeit.default_timer() - start_time 


# In[148]:


print('pi_monte_carlo took', time_1)
print('Python solution took', time_2)


# In[ ]:




