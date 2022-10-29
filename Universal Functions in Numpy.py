#!/usr/bin/env python
# coding: utf-8

# # Universal Functions (ufunc) in Numpy examples
# 
# ##These functions operate element wise in the array, producing another array as output

# In[12]:


from numpy import sqrt           ## importing sqrt method from numpy module

arr1d=[3,20,36,46,51,9]         ##creating 1 d array
newarr=sqrt([arr1d])           ##using sqrt  universal function
print(newarr)
    


# In[42]:


##sine ufunc

import numpy as np
np.sin([0,90,45])            # sine function 


# In[38]:


## cos ufunc

np.cos(0)                    # cosine function


# In[41]:


## floor ufunc

np.floor([1.2,3.4,5.6,-1.6,-5.8,4.1,5]) # floor ufunc returns largest integrer value of every elemnt in the arry


# In[ ]:




