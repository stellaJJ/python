#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
get_ipython().run_line_magic('precision', '3')


# In[3]:


df=pd.read_csv('../python_stat_sample-master/data/ch2_scores_em.csv',
               index_col='student number')
df.head()


# In[4]:


scores=np.array(df['english'])[:10]
scores


# In[5]:


scores_df=pd.DataFrame({'score':scores},
                        index=pd.Index(['A','B','C','D','E','F','G','H','I','J'],
                        name='student'))

scores_df


# In[10]:


#평균
sum(scores)/len(scores)


# In[7]:


np.mean(scores)


# In[8]:


scores_df.mean()


# In[9]:


#중앙값
sorted_scores=np.sort(scores)
sorted_scores


# In[13]:


n=len(sorted_scores)
if n%2==0:
    m0=sorted_scores[n//2-1]
    m1=sorted_scores[n//2]
    median=(m0+m1)/2
else:
    median=sorted_scores[(n+1)//2-1]

median


# In[14]:


np.median(scores)


# In[15]:


scores_df.median()


# In[16]:


#최빈값
pd.Series([1,1,1,2,2,3]).mode()


# In[17]:


pd.Series([1,2,3,4,5]).mode()


# In[26]:


#분산과 표준편차
#편차
mean=np.mean(scores)
deviation=scores-mean
deviation


# In[19]:


another_scores=[50,60,58,54,51,56,57,53,52,59]
another_mean=np.mean(another_scores)
another_deviation=another_scores-another_mean
another_deviation


# In[20]:


np.mean(deviation)


# In[21]:


np.mean(another_deviation)


# In[22]:


summary_df=scores_df.copy()
summary_df['deviation']=deviation
summary_df


# In[23]:


summary_df.mean()


# In[27]:


#분산
np.mean(deviation**2)


# In[25]:


np.var(scores)


# In[28]:


scores_df.var()


# In[29]:


summary_df['square of deviation']=np.square(deviation)
summary_df


# In[30]:


summary_df.mean()


# In[34]:


#표준편차
np.sqrt(np.var(scores,ddof=0)) #ddof 는 표준분산


# In[32]:


np.std(scores,ddof=0)


# In[35]:


np.max(scores)-np.min(scores)


# In[37]:


scores_Q1=np.percentile(scores,25)
scores_Q3=np.percentile(scores,75)
scores_IQR=scores_Q3-scores_Q1 #사분위 번위
scores_IQR


# In[38]:


#데이터 지표정리
pd.Series(scores).describe()


# In[39]:


#표준화
z=(scores-np.mean(scores)) /np.std(scores)
z


# In[40]:


np.mean(z),np.std(z,ddof=0)


# In[41]:


z=50+10*(scores-np.mean(scores)) /np.std(scores)
z


# In[42]:


scores_df['deviation value']=z
scores_df


# In[43]:


#데이터의 시각화
english_scores=np.array(df['english'])
pd.Series(english_scores).describe() #series 로 변환하여 describe 표시


# In[44]:


#도수분포표
freq,_=np.histogram(english_scores,bins=10,range=(0,100))
freq


# In[46]:


freq_class=[f'{i}~{i+10}' for i in range(0,100,10)]
freq_dist_df=pd.DataFrame({'frequency':freq},
                          index=pd.Index(freq_class,name='Class'))
freq_dist_df


# In[48]:


for a in range(7):
    print(a)


# In[49]:


for a in range(10,5,-1):
    print(a)


# In[52]:


total=0
for i in range(1,10):
    total+=i
print(total)


# In[53]:


total=0
for i in range(1,10,2):
    total+=i
print(total)


# In[63]:


#계급값: 각 계급을 대표하는 값(중앙값이용)
class_value=[(i+(i+10))//2 for i in range(0,100,10)] #for문에서 0부터 90까지 10간격 수열생성
                                                     #생성된 숫자에서 각 i 가 0,10,20변경되면서 0-10,10-20 구간 중간값을 계산한 값을 변수에 저장
class_value


# In[60]:


#상대도수
rel_freq=freq/freq.sum()
rel_freq


# In[61]:


#누적 상대도수
cum_rel_freq=np.cumsum(rel_freq)
cum_rel_freq


# In[64]:


#계급값,상대도수,누적상대도수를 도수분포표에 추가
freq_dist_df['class value']=class_value
freq_dist_df['relative frequency']=rel_freq
freq_dist_df['cumulative relative frequency']=cum_rel_freq
freq_dist_df=freq_dist_df[['class value','frequency', 'relative frequency', 'cumulative relative frequency']]
freq_dist_df


# In[65]:


freq_dist_df.loc[freq_dist_df['frequency'].idxmax(),'class value']


# In[70]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[73]:


fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot(111)
freq, _, _ =ax.hist(english_scores,bins=10,range=(0,100))
ax.set_xlabel('score')
ax.set_ylabel('person number')
ax.set_xticks(np.linspace(0,100,10+1))
ax.set_yticks(np.arange(0,freq.max()+1))
plt.show()


# In[75]:


fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot(111)
freq, _, _ =ax.hist(english_scores,bins=25,range=(0,100))
ax.set_xlabel('score')
ax.set_ylabel('person number')
ax.set_xticks(np.linspace(0,100,25+1))
ax.set_yticks(np.arange(0,freq.max()+1))
plt.show()


# In[82]:


fig=plt.figure(figsize=(10,6))
ax1=fig.add_subplot(111)
ax2=ax1.twinx()
weights =np.ones_like(english_scores) /len (english_scores)
rel_freq, _, _ =ax1.hist(english_scores, bins=25,range=(0,100),weights=weights)

cum_rel_freq=np.cumsum(rel_freq)
class_value=[(i+(i+4))//2 for i in range(0,100,4)]

ax2.plot(class_value, cum_rel_freq, ls='--', marker='o',color='gray')
ax2.grid(visible=False)#눈금제거

ax1.set_xlabel('score')
ax1.set_ylabel('relative frequency')
ax2.set_ylabel('cumulative relative frequency')
ax1.set_xticks(np.linspace(0,100,25+1))

plt.show()


# In[84]:


#상자그림
fig=plt.figure(figsize=(5,6))
ax=fig.add_subplot(111)
ax.boxplot(english_scores, tick_labels=['english'])
plt.show()


# In[85]:


fig=plt.figure()
ax1=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)
x=range(0,100)
y=[v*v for v in x]
ax1.plot(x,y)
ax2.bar(x,y)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




