
# coding: utf-8

# In[1]:


import numpy as np


# ** Create an array **

# In[2]:


np.arange(5)


# In[5]:


np.arange(4,7)


# In[6]:


np.arange(3, 22, 2)


# In[7]:


np.linspace(0, 10,100)


# In[13]:


np.logspace(0,5,10)


# # Reshaping arrays

# In[15]:


x = np.arange(12)


# In[16]:


x


# In[18]:


x.reshape(4,3)


# In[19]:


x.reshape(6, -1)


# # Get the size and the shape

# In[20]:


x


# In[21]:


x.size


# In[23]:


x.reshape(4, 3).shape


# In[24]:


x.any()


# In[25]:


x.all()


# In[27]:


np.array([]).any()


# In[28]:


np.array([])


# # Transpose

# In[29]:


x.reshape(4,3)


# In[30]:


x.reshape(4,3).T


# # Maths

# In[33]:


y = x.reshape(4, 3)


# In[34]:


y


# In[35]:


y + 5


# In[36]:


z = np.arange(4).reshape(4,1)


# In[37]:


z


# In[38]:


y


# In[39]:


y + z


# # Statistical Summary

# In[40]:


x 


# In[41]:


x.sum()


# In[42]:


x.mean()


# In[43]:


x.max()


# In[44]:


x.min()


# In[45]:


x.std()


# In[46]:


x.prod()


# In[47]:


k = [22, 3, 33]


# In[49]:


x[1:].prod()

