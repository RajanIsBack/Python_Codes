#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


x=[1,3,5,7]
[10*i for i in x]


# In[5]:


nparray=np.array(x)
nparray


# In[8]:


#pass list of lists
x=[[3.1,2,4],[1.4,5,6]]
nparray=np.array(x)
nparray
nparray.shape


# In[12]:


nparray=np.zeros(10)
nparray


# In[14]:


nparray1=np.ones(5)
nparray1
    


# In[17]:


x=[1.2,3.4,5.6]
nparray=np.array(x)
print "last element",nparray[-1]
print "first two element",nparray[:2]
print "last2 element",nparray[-2:]



# In[20]:


np2d=np.array([[1,2,3],[3,4,5],[5,6,7]])
np2d
print "np2d11",np2d[1][1]
print "np2d1",np2d[1]


# In[30]:


x=[1,2,3,4,5,6,7,8,9,10]
nparray=np.array(x)
y=nparray.reshape((5,2))
print "y",y
y.flatten()


# In[35]:


nparray1=[1,2,3]
nparray2=[4,5,6]
np.concatenate((nparray1,nparray2),axis=0)


# In[38]:


nparray1=([[1,2,3,4],[4,6,7,8]])
nparray2=([[1.1,2,3,4],[4.1,6,7,8]])
np.concatenate((nparray1,nparray2),axis=1)

