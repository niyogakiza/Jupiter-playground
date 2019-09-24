
# coding: utf-8

# In[1]:


import numpy as np


# In[7]:


x = [list(range(0,6)), list(range(9,15)), list(range(20,26))]


# In[8]:


x


# In[10]:


xnp = np.array(x)


# In[11]:


xnp


# ** Indexing **

# In[15]:


x[0]


# In[16]:


x[3]


# In[17]:


x[2]


# In[18]:


x[2][1]


# In[19]:


xnp[2, 3]


# ** Slicing **
# 

# In[22]:


x[0:1, 3:4] 


# In[23]:


# Doesn't understand it because x is a list doesn't have rows and columns


# In[29]:


xnp[0:2, 1:4]


# In[38]:


xnp[0:2, 1:3]


# In[39]:


xnp[2:3]


# In[40]:


xnp[0:3, 2:3]


# In[42]:


xnp[0:4, 2:4]


# ** Logical Indexing **

# In[44]:


xnp > 10


# In[45]:


xnp[xnp > 10]


# In[46]:


xnp[:, 2]


# In[47]:


xnp[:, 2] > 10


# In[48]:


xnp[:, 2][xnp[:, 2] > 10]


# In[49]:


xnp[:, 3]


# In[50]:


xnp[2, :]

