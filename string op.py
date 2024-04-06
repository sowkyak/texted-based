#!/usr/bin/env python
# coding: utf-8

# In[6]:


a ="HELLO"
print(a)


# In[ ]:





# In[2]:


b = "Hello world"
len(b)


# In[5]:


a ="Hello"
b = "World"
c =a+ "" +b
print(c)


# In[33]:


a =  "   Hello"
print(a.lower())


# In[12]:


a.lstrip()


# In[32]:


c="/////Hello world"
c.lstrip('/')


# In[37]:


a = "Peter prince"
b= a.endswith("prince"), a.startswith("Peter")
b


# In[34]:


b = "How are You"
b.find("How")


# In[26]:


b.replace("You","you")


# In[35]:


a = "Rise and shine "
a.split()


# In[38]:


str = " apple banana blueberry cherry"
token = str.split()
token


# In[39]:


st = "1/3/5/8/39/5"
list = st.split('/')
list


# # Regular exp

# In[49]:


import regex as re
def tokenize(text):
    return re.findall(r'abc',text)
x=tokenize("abcd 45abc abc% abc.com acbrx .=.abc.=ab c cba ABC")
x


# In[52]:


import regex as re
def tokenize(text):
    return re.findall(r"bindu",text)
def tokenize2(text):
    return re.findall(r"bindu alekhya",text)
x = tokenize("sowkya bindu alekhya bindu bindu ammu")
print(x)
y= tokenize2("bindu alekya bindu sowkya bindu ammu")
print(x)


# In[ ]:




