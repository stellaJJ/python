#!/usr/bin/env python
# coding: utf-8

# In[1]:


#7주차 코드

import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('precision', '3')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


x_set= np.array([1,2,3,4,5,6,])


# In[5]:


#확률변수 구현

def f(x):
    if x in x_set:
        return x/21
    else:
        return 0


# In[6]:


X=[x_set, f]


# In[7]:


prob=np.array([f(x_k) for x_k in x_set])

dict(zip(x_set, prob))


# In[9]:


fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot(111)
ax.bar(x_set, prob)
ax.set_xlabel('value')
ax.set_ylabel('probability')

plt.show()


# In[10]:


np.all(prob>=0)


# In[11]:


np.sum(prob)


# In[12]:


a={'사과':1, '딸기':5,'귤':10}
a


# In[14]:


a={('초콜릿',200):20, ('마카롱',500):15, ('쿠키',300):30}
a


# In[15]:


a={'사과':1 , '딸기':5 ,'귤':10}
v1=a['딸기']
v1


# In[60]:


#v2=a['레몬']
#v2


# In[17]:


f1='딸기' in a 
f1


# In[18]:


f2='레몬' not in a 
f2


# In[19]:


f3='레몬' in a
f3


# In[20]:


v1=a.get('딸기')
v1


# In[22]:


v2=a.get('레몬')
v2


# In[23]:


a={'초콜릿':1, '마카롱':2, '쿠키':3}
a['초콜릿']='One'
a['마카롱']='Two'
a['쿠키']='Three'
a


# In[24]:


d=dict(초콜릿=20, 마카롱=15, 쿠키=30)
d


# In[25]:


key=['초콜릿', '마카롱' , '쿠키']
value=[20,15,30]
d=dict(zip(key, value))
d


# In[26]:


d=dict([('초콜릿', 20), ('마카롱', 15), ('쿠키',30)])
d


# In[30]:


def F(x):
    return np.sum([f(x_k) for x_k in x_set if x_k <=x])
    #x_k가 뭔지 모르겠네 x가 될 수 잇는 변수인건가

F(3) # x=1, x=2, x=3일 때의 확률을 모두 더하는 것임


# In[33]:


#확률 변수를 2x+3으로 변환해도 이전에 x와 같은 결과가 나온다!!!
#그리고 x_k는 그냥 확률 변수 X를 의미하는 for 변수인듯(i처럼)

y_set=np.array([2*x_k +3 for x_k in x_set])
prob=np.array([f(x_k) for x_k in x_set])
dict(zip(y_set, prob))


# In[47]:


np.sum([x_k *f(x_k) for x_k in x_set])


# In[48]:


sample=np.random.choice(x_set, int(1e6), p=prob)
np.mean(sample)


# In[53]:


def E(X, g=lambda x: x):
    x_set, f=X
    return np.sum([g(x_k)*f(x_k) for x_k in x_set])

E(X) #시험에 내진 않았단다..람다함수


# In[42]:


#numpy.random.choice(a, size=None, replace=True, p=None)
#a : 배열이면 원래의 데이터 / 정수면 arange(a)로 데이터 생성
#size: 정수. 샘플숫자
#replace: 불리언, true면 한 번 선택한 데이터 다시 선택 가능
#p: 배열. 각 데이터가 선택될 수 있는 확률.


# In[43]:


np.random.choice(5,5, replace =False)


# In[44]:


np.random.choice(5,3,replace=False)


# In[45]:


np.random.choice(5,10)


# In[46]:


np.random.choice(5,10, p=[0.1,0,0.3,0.6,0])


# In[54]:


mean=E(X)
np.sum([(x_k-mean)**2 *f(x_k) for x_k in x_set])


# In[56]:


def V(X, g=lambda x: x):
    x_set, f=X
    mean= E(X, g)
    return np.sum([(g(x_k)-mean)**2 *f(x_k) for x_k in x_set])

V(X)


# In[57]:


V(X, lambda x: 2*x +3)


# In[58]:


2**2 * V(X)


# In[ ]:




