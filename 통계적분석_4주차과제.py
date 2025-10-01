#!/usr/bin/env python
# coding: utf-8

# In[36]:


import numpy as np
import pandas as pd
get_ipython().run_line_magic('precision', '3')


# In[37]:


df=pd.read_csv('../python_stat_sample-master/data/ch2_scores_em.csv',
               index_col='student number')


# In[38]:


en_scores=np.array(df['english'])[:10]
ma_scores=np.array(df['mathematics'])[:10]
scores_df=pd.DataFrame({'english': en_scores,
                        'mathematics': ma_scores},
                       index=pd.Index(['A','B','C','D','E',
                                       'F','G','H','I','J'], name='student'))
scores_df


# In[39]:


summary_df=scores_df.copy()
summary_df['english_deviation']=\
    summary_df['english']-summary_df['english'].mean()
summary_df['mathematics_deviation']=\
    summary_df['mathematics']-summary_df['mathematics'].mean()
summary_df['product of deviations']=\
    summary_df['english_deviation']*summary_df['mathematics_deviation']
summary_df


# In[40]:


summary_df['product of deviations'].mean()


# In[41]:


cov_mat=np.cov(en_scores, ma_scores, ddof=0)
cov_mat


# In[42]:


cov_mat[0,0], cov_mat[1,1]


# In[43]:


np.var(en_scores, ddof=0), np.var(ma_scores, ddof=0)


# In[44]:


cov_mat[0,1], cov_mat[1,0]


# In[45]:


np.cov(en_scores, ma_scores, ddof=0)[0,1]/\
(np.std(en_scores)*np.std(ma_scores))


# In[47]:


np.corrcoef(en_scores, ma_scores)


# In[48]:


scores_df.corr()


# In[49]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[51]:


#산점도
english_scores=np.array(df['english'])
math_scores=np.array(df['mathematics'])

fig=plt.figure(figsize=(8,8))
ax=fig.add_subplot(111)
ax.scatter(english_scores, math_scores)
ax.set_xlabel('english')
ax.set_ylabel('mathematics')

plt.show()


# In[53]:


#회귀직선
poly_fit=np.polyfit(english_scores, math_scores,1)
poly_1d=np.poly1d(poly_fit)
xs=np.linspace(english_scores.min(), english_scores.max())
ys=poly_1d(xs)

fig=plt.figure(figsize=(8,8))
ax=fig.add_subplot(111)
ax.set_xlabel('english')
ax.set_ylabel('mathematics')
ax.scatter(english_scores, math_scores, label='score')
ax.plot(xs, ys, color='gray', label=f'{poly_fit[1]: .2f}+{poly_fit[0]:.2f}x')
ax.legend(loc='upper left')
plt.show()


# In[54]:


fig=plt.figure(figsize=(10,8))
ax=fig.add_subplot(111)

c=ax.hist2d(english_scores, math_scores, bins=[9,8], range=[(35,80), (55,95)])
ax.set_xlabel('english')
ax.set_ylabel('mathematics')
ax.set_xticks(c[1])
ax.set_yticks(c[2])
fig.colorbar(c[3], ax=ax)
plt.show()


# In[56]:


anscombe_data=np.load('../python_stat_sample-master/data/ch3_anscombe.npy')
print(anscombe_data.shape)
anscombe_data[0]


# In[65]:


stats_df=pd.DataFrame(index=['X_mean', 'X_variance', 'Y_mean', 'Y_variance','X&Y_correlation', 
                      'X&Y_regression line'])
for i, data in enumerate(anscombe_data):
    dataX=data[:,0]
    dataY=data[:,1]
    poly_fit=np.polyfit(dataX, dataY,1 )
    stats_df[f'data{i+1}']=\
        [f'{np.mean(dataX):.2f}',
        f'{np.var(dataX):.2f}',
        f'{np.mean(dataY):.2f}',
        f'{np.var(dataY):.2f}',
        f'{np.corrcoef(dataX,dataY)[0,1]:.2f}',
        f'{poly_fit[1]:.2f} + {poly_fit[0]:.2f}x']
stats_df


# In[69]:


fig,axes=plt.subplots(nrows=2, ncols=2, figsize=(10,10),
                      sharex=True, sharey=True)
xs=np.linspace(0,30,100)
for i, data in enumerate(anscombe_data):
    poly_fit=np.polyfit(data[:,0], data[:,1], 1)
    poly_1d=np.poly1d(poly_fit)
    ys=poly_1d(xs)

    ax=axes[i//2, i%2]
    ax.set_xlim([4,20])
    ax.set_ylim([3,13])

    ax.set_title(f'data{i+1}')
    ax.scatter(data[:,0], data[:,1])
    ax.plot(xs,ys,color='gray')

    plt.tight_layout()
    plt.show()


# In[70]:


#추측통계
df=pd.read_csv('../python_stat_sample-master/data/ch4_scores400.csv')
scores=np.array(df['score'])
scores[:10]


# In[76]:


#표본추출방법
np.random.choice([1,2,3],3)


# In[75]:


np.random.choice([1,2,3],3,replace=False)


# In[77]:


np.random.seed(0)
np.random.choice([1,2,3],3)


# In[78]:


np.random.seed(0)
sample=np.random.choice(scores,20)
sample.mean()


# In[79]:


scores.mean()


# In[80]:


for i in range(5):
    sample=np.random.choice(scores,20)
    print(f'{i+1}번째 무작위 추출로 얻은 표본평균', sample.mean())


# In[84]:


#확률분포
dice=[1,2,3,4,5,6]
prob=[1/21,2/21,3/21,4/21,5/21,6/21]


# In[85]:


num_trial=100
sample=np.random.choice(dice, num_trial, p=prob)
sample


# In[89]:


#계급폭 1점 히스토그램
fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot(111)
ax.hist(scores, bins=100, range=(0,100), density=True)
ax.set_xlim(20,100)
ax.set_ylim(0,0.042)
ax.set_xlabel('score')
ax.set_ylabel('relative frequency')
plt.show()


# In[91]:


np.random.choice(scores)


# In[92]:


sample=np.random.choice(scores,10000)

fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot(111)
ax.hist(sample, bins=100, range=(0,100), density=True)
ax.set_xlim(20,100)
ax.set_ylim(0,0.042)
ax.set_xlabel('score')
ax.set_ylabel('relative frequency')
plt.show()


# In[102]:


sample_means=[np.random.choice(scores,20).mean()
              for _ in range(10000)] #for 앞뒤에 띄어쓰기 필요, 반복변수에 의미가 딱히 필요없을 때 _사용

fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot(111)
ax.hist(sample_means, bins=100, range=(0,100), density=True)
#모평균 세로선으로 표시
ax.vlines(np.mean(scores),0,1,'gray')
ax.set_xlim(50,90)
ax.set_ylim(0,0.13)
ax.set_xlabel('score')
ax.set_ylabel('relative frequency')
plt.show()

