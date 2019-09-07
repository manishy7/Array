#!/usr/bin/env python
# coding: utf-8

# In[ ]:


A=[2,3,1,5]
q=len(A)
m=min(A)
w=max(A)
w=w+1

l=list()
for i in range(m,w):
    l.append(i)
z=[i for i in l if i not in A]
r=len(z)
o=z[r-1]
print(o)

