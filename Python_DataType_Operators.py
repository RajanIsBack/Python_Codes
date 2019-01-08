#!/usr/bin/env python
# coding: utf-8

# In[1]:


x="Hello Python"
print x


# In[2]:


a=1
b=3
print a+b


# In[3]:


a='1'
b='2'
print a+b


# In[4]:


a='1'
b='2'
print int(a)+int(b)


# In[10]:


x=15.4
print 'type of x is ',type(x)

y=True
print 'type of y is ',type(y)

z='stringstype'
print 'type of z is',type(z)


# In[7]:


#operstors in python
print 3+4
print 3-2
print 3*4
print 3%2


# In[11]:


#list ordered,variuos types
x=[1,2,3]
print x
type(x)


# In[12]:


x=[1.1,3.6,6.34]
print x
type(x)


# In[17]:


x=[1,1.1,'test',True,[1,2,3]]
print x
type(x)


# In[25]:


#dictionary
x={"a": 1,"b": 4.45,"c": "A string"}
x['key'] = 'A new value'
print x
type(x)

x.keys()

y=[]
print y



# In[35]:


x=[1.1,4.34,7.8]
print x
print x[0]
print x[1]
print x[2]

x[1]= 23.556
print x
print x[-1] #print x[-1] 
print x[:2]

x.append(8)
print x

x.remove(8)
print x


# In[36]:


x=[1,2,3]
y=[4,5,6]
print x+y


# In[37]:


#tuples

x=(1,2)
print x
print type(x)


# In[38]:


x=(1,2)
print x[1]
x[1]=3 # TypeError: 'tuple' object does not support item assignment

