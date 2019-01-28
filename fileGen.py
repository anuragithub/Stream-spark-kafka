#!/usr/bin/env python
# coding: utf-8

# In[10]:


import time


# In[11]:


output_file = "D:/Mlprojects/quartic_ai/mle_task/test.txt"


# In[12]:


input_file = "D:/Mlprojects/quartic_ai/mle_task/test.csv"


# In[13]:


def writeLine(line):
    with open(output_file,"a") as f:
        f.write(line)


# In[14]:


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


# In[16]:


with open(input_file,"r") as f:
    lines =file_len(input_file)
    for x in range(1,lines):
        line = f.readline(x)
        writeLine(line)
        time.sleep(5)


# In[ ]:





# In[ ]:




