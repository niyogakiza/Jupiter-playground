
# coding: utf-8

# In[4]:


import numpy as np


# In[5]:


x = [150, 200, 300, 450]


# In[6]:


x


# In[7]:


y = np.array(x)


# In[8]:


y


# In[9]:


type(x)


# In[10]:


type(y)


# In[11]:


x + x


# In[12]:


x* 3


# In[13]:


y + y


# In[14]:


y + 3


# In[15]:


y[0]


# In[16]:


y[0:4]


# In[17]:


y[:3]


# In[18]:


y[:1]


# In[19]:


y[-1]


# In[20]:


y[-3:-1]


# **Logical indexing**

# In[22]:


y > 200


# In[23]:


y == 300


# In[24]:


y != 200


# In[25]:


y[y > 200]

