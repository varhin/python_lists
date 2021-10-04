#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# python list is defined by square brackets.
list_1 = []


# In[ ]:


# a list containing differents types of data
list_1 = ['my name', 3, True, 4.6]


# In[5]:


#accessing items in a list
list_1 = ['my name', 3, True, 4.6]
list_1[0]


# In[8]:


#negative indexing
list_1 = ['my name', 3, True, 4.6]
list_1[-1]


# In[7]:


#selecting a range of items
list_1 = ['my name', 3, True, 4.6]
list_1[1:3]


# In[9]:


#duplicate items 
list_2 = ['red','white','cyan','white','black']
list_2


# In[12]:


#length of a list
list_2 = ['red','white','cyan','white','black']
len(list_2)


# In[6]:


list_2 = ['red','white','cyan','white','black']
print(type(list_2))


# In[8]:


#joining list using the plus operator.
list_1 = ['my name', 3, True, 4.6]
list_2 = ['red','white','cyan','white','black']
list_1 + list_2


# In[15]:


#joining list using the append method.
list_1 = ['my name', 3, True, 4.6]
list_2 = ['red','white','cyan','white','black']
list_1.append(list_2)
print(list_1)


# In[13]:


#joining list using the extend method.
list_1 = ['my name', 3, True, 4.6]
list_2 = ['red','white','cyan','white','black']
list_1.extend(list_2)
print(list_1)

