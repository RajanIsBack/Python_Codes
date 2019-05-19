#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np

c=[1,2,3,4]

arr=np.array(c)
arr


# In[10]:


arr=np.array([11,22,33,44])
arr
print (type(arr))
print (arr.shape)


# In[12]:


data=([11,12],[13,14])
arr2d=np.array(data)
print(arr2d)
print(arr2d.shape) 
print(arr2d.ndim)


# In[18]:


#difference between list and array
list1=[1,2,3]
print("List appends that much element",list1*2)

arr1=np.array([1,2,3])
print("Array works element by element",arr1*2)

print("*"*20)
a=[1,2,3]
b=[4,5,6]
print ("list adds",a+b)
arr1=np.array([1,2,3])
arr2=np.array([4,5,5])
print("array adds element by element",(arr1+arr2))


# In[25]:


#arrange function(sttart,stop,step)
print(np.arange(2,20,3))
print("*"*40)
print(np.arange(50))


# In[29]:


#np.zeros and np.ones

arr1=np.zeros([2,3])
print(arr1)
print("*"*40)
# array datatype
print(arr1.dtype)
print("*"*40)
arr1=np.ones([5,3])
print(arr1)


# In[31]:


#array shape
arr1.shape


# In[32]:


#array of dtype integer
arr1=np.ones([5,3],dtype=int)
arr1


# In[33]:


#np.linspace(start,stop,number of elements you want lienearly seperated)

arr2=np.linspace(0,20,6)
arr2


# ## Array Reshaping using reshape and flattening using ravel

# In[49]:


#restructure/shape the array
arr=np.arange(24)
print(arr)
print(arr.ndim)

print("#"*20)
arr1=arr.reshape(2,12)
print(arr1)
print("DImension",arr1.ndim)

print("#"*20)
arr2=arr.reshape(2,3,4)#2times 3*4 arrays
print(arr2)
print("DImension",arr2.ndim)


# In[56]:


#flatten higher dimension into single dimension using ravel
arr3d=arr2
print("arr3d",arr3d)
arr1d=arr2.ravel()
print(arr1d)
print("Dimension",arr1d.ndim)


# ## Indexing in array

# In[57]:


arr=np.array([11,22,3,4,5,7,87,45])
arr[0]


# In[61]:


arr[[1,3]]


# In[63]:


arr[[1,5]]


# In[70]:


arr=np.array([1,2,3,4,5,6,7,8,9])
arr_slice= slice(1,7,2)
arr[arr_slice]


# In[75]:


arr=np.arange(20)
print(arr)
#arr[1],arr[3],arr[5],arr[7],arr[9]
arr1=arr[1:10:2]
print(arr1)


# In[79]:


arr2=np.array([3,4,6,7,8,9,12,23,3445,567])
print(arr2[:2])#from index 0 to 1


# In[84]:


arr2d=np.array([[1,4,546,6,345],
               [23,34,45,56,67]])
print(arr2d)
print("DImension",arr2d.ndim)


# ## Loading data fom text using numpy

# In[114]:


arr4=np.loadtxt(r'C:\Users\Rajan Kumar\Documents\Python_Sundog\DataScience\EdurekaCodePython\textfile.txt')
print(arr4)
print(arr4.dtype)


# In[117]:


arr5=np.loadtxt(r'C:\Users\Rajan Kumar\Documents\Python_Sundog\DataScience\EdurekaCodePython\textfile.txt',dtype=int)
print(arr5)


# In[116]:


help(np.loadtxt)


# In[119]:


arr5=np.loadtxt(r'C:\Users\Rajan Kumar\Documents\Python_Sundog\DataScience\EdurekaCodePython\textfile.txt',dtype=int,skiprows=2)
print(arr5)


# In[146]:


arr6=np.loadtxt(r'C:\Users\Rajan Kumar\Documents\Python_Sundog\DataScience\EdurekaCodePython\textfile.txt',dtype=int,skiprows=2)
print(arr6)
print("*"*30)
arr7=np.loadtxt(r'C:\Users\Rajan Kumar\Documents\Python_Sundog\DataScience\EdurekaCodePython\textfile.txt',dtype=int)
print(arr7)
print("*"*0)


# In[144]:



arr8=[[1,2,3,4,5],
     [23,23,434,45,3]]
print (arr8)


# In[142]:


#saving to text file
np.savetxt(r'C:\Users\Rajan Kumar\Documents\Python_Sundog\DataScience\EdurekaCodePython\output.txt',arr8,fmt='%.3f')


# ## Read csv

# In[173]:


arrcsv=np.genfromtxt(r'C:\Users\Rajan Kumar\Documents\Python_Sundog\DataScience\EdurekaCodePython\brain_size.csv',delimiter=';',skip_header=1)
print(arrcsv)
np.savetxt(r'C:\Users\Rajan Kumar\Documents\Python_Sundog\DataScience\EdurekaCodePython\mytxtopfile.csv',arr,delimiter=";")


# In[ ]:





# In[ ]:




