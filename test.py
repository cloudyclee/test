#!/usr/bin/env python
# coding: utf-8

# In[14]:


## 1A 反轉字串

def rev(str):
    l = len(str)
    x = ""
    while l != 0 :
        p = l-1
        x = x + str[p]
        l = l-1
    return x

print(rev("dog is good"))


# In[22]:


## 1B 反轉單字

def rev(str):
    temp = str.split(" ")
    ans = []
    for v in temp:
        l = len(v)
        x = ""
        while l != 0 :
            p = l-1
            x = x + str[p]
            l = l-1
        ans.append(x + " ")
    return ans

print(rev("dog is good"))


# In[7]:


## 2 篩選機

def f(n):
    x = []
    for i in range(n+1):
        if(i % 3 and i % 5 != 0 or i % 15 == 0):
            x.append(i)
    l = len(x) - 1
    return(l)

f(15)


# In[ ]:


## 3 分辨袋子

因為標籤都是錯的，所以打開其中一個袋子後，就可以知道剩下兩袋裝的內容物和剩下的兩個標籤，標籤和內容物不能配對正確，就只有一種配法了

拿到裝鉛筆的袋子：
上面寫原子筆：另外寫鉛筆的袋子裝鉛筆和原子筆，寫原子筆和鉛筆的袋子裝原子筆
上面寫原子筆和鉛筆：另外寫鉛筆的袋子裝原子筆，寫原子筆的袋子裝鉛筆和原子筆

拿到裝原子筆的袋子：
上面寫鉛筆：另外寫原子筆的裝的是鉛筆和原子筆，寫鉛筆和原子筆裝的是鉛筆
上面寫鉛筆和原子筆；：另外寫原子筆的袋子裝鉛筆，寫鉛筆的袋子裝原子筆和鉛筆

拿到裝鉛筆和原子筆的袋子：
上面寫鉛筆：另外寫原子筆的袋子裝鉛筆，寫鉛筆和原子筆的袋子裝原子筆
上面寫原子筆：另外寫鉛筆和原子筆的袋子裝鉛筆，另外寫鉛筆的袋子裝原子筆


# In[ ]:


## 4 找錢問題

這兩項香家沒有任何意義，810和70相加的不代表他們付出的總金額

