#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

get_ipython().run_line_magic('precision', '3')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.read_csv('../python_stat_sample-master/data/ch4_scores400.csv')
scores=np.array(df['score'])
scores[:10]


# In[3]:


np.random.choice([1,2,3],3)


# In[12]:


np.random.choice([1,2,3],3,replace=False)


# In[8]:


np.random.seed(0)
np.random.choice([1,2,3],3)
#seed를 주면 값이 같게 나옴


# In[13]:


np.random.seed(0)
sample=np.random.choice(scores,20)
sample.mean()


# In[14]:


scores.mean()


# In[15]:


for i in range(5):
    sample=np.random.choice(scores,20)
    print(f'{i+1}번째 무작위 추출로 얻은 표본평균', sample.mean())


# In[17]:


#불공정한 주사위 확률분포
dice=[1,2,3,4,5,6]
prob=[1/21,2/21,3/21,4/21,5/21,6/21]
np.random.choice(dice, p=prob)


# In[19]:


num_trial=100 #100번 시도
sample=np.random.choice(dice,num_trial, p=prob)
sample


# In[22]:


freq, _=np.histogram(sample, bins=6, range=(1,7))
pd.DataFrame({'frequency':freq,
              'relative frequency': freq /num_trial},
             index=pd.Index(np.arange(1,7), name='dice'))


# In[24]:


fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot(111)
ax.hist(sample, bins=6, range=(1,7), density=True, rwidth=0.8)
ax.hlines (prob, np.arange(1,7), np.arange(2,8), colors='gray')

ax.set_xticks(np.linspace(1.5,6.5,6))
ax.set_xticklabels(np.arange(1,7))
ax.set_xlabel('dice')
ax.set_ylabel('relative frequency')
plt.show()


# In[26]:


#횟수를 100이 아니라 10000으로 늘리면 실제 분포에 비슷하게 나온다. 
num_trial=10000
sample=np.random.choice(dice, size=num_trial, p=prob)

fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot(111)
ax.hist(sample, bins=6, range=(1,7), density=True, rwidth=0.8)
ax.hlines (prob, np.arange(1,7), np.arange(2,8), colors='gray')

ax.set_xticks(np.linspace(1.5,6.5,6))
ax.set_xticklabels(np.arange(1,7))
ax.set_xlabel('dice')
ax.set_ylabel('relative frequency')
plt.show()


# In[27]:


fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot(111)
ax.hist(scores, bins=100, range=(0,100), density=True)

ax.set_xlim(20,100)
ax.set_ylim(0, 0.042)

ax.set_xlabel('score')
ax.set_ylabel('relative frequency')
plt.show()


# In[28]:


np.random.choice(scores)


# In[30]:


#표본크기가 20인 표본 10000번 수행

sample_means=[np.random.choice(scores, 20).mean()
              for _ in range(10000)]


fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot(111)
ax.hist(scores, bins=100, range=(0,100), density=True)
  
#모평균을 세로선으로 표시
ax.vlines(np.mean(scores),0,1,'gray')
ax.set_xlim(50,90)
ax.set_ylim(0, 0.13)
ax.set_xlabel('score')
ax.set_ylabel('relative frequency')
plt.show()


# In[ ]:




