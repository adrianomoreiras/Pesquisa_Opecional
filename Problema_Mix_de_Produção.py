#!/usr/bin/env python
# coding: utf-8

# In[2]:


from pulp import *


# In[8]:


# Dados do problema
#Tempos das Atividades x produtos
tempos = [[2,5,5,0,0],
         [5,5,0,2,2],
         [6,7,0,10,2],
         [0,0,4,2,0],
         [0,1,7,0,0],
         [0,0,3,0,4],
         [0,5,2,0,4],
         [0,0,10,0,1],
         [0,4,3,8,0],
         [3,0,0,0,3]]


# In[4]:


#Tipos de produtos
produto = [0,1,2,3,4,5,6,7,8,9]


# In[5]:


maximo = {0:300.5,
         1:200.5,
         2:150,
         3:180,
         4:220,
         5:200.5,
         6:160,
         7:300,
         8:150,
         9:200}


# In[6]:


lucro = {0:1.2,
         1:2.3,
         2:3.4,
         3:2,
         4:3,
         5:1.9,
         6:0.6,
         7:1,
         8:2,
         9:3}


# In[9]:


capacidades = {0:4000,
              1:5000,
              2:3000,
              3:7000,
              4:2500}


# In[10]:


volume_total = 1000


# In[11]:


#Criação das variaveis de decisão
var = LpVariable.dict("C", (produto),lowBound=0)


# In[12]:


#Criação do modelo
model = LpProblem("Problema_mix_prdução", LpMaximize)


# In[14]:


lista_fo = []


# In[15]:


for x in produto:
    lista_fo.append(var[x]*lucro[x])


# In[16]:


model += lpSum(lista_fo)
print(model)


# In[21]:


#Criação das restrições
lista_rest = []
for i in capacidades.keys():
    for j in produto:
        if tempos [j][i]!=0:
            lista_rest.append(var[j]*tempos[j][i])
        else:
            None
    model += lpSum(lista_rest) <= capacidades[i]
    lista_rest = []
print(model)


# In[23]:


for x in var.keys():
    model += var[x] <= maximo[x]


# In[25]:


for x in var.values():
    lista_rest.append(x)


# In[26]:


model += lpSum(lista_rest) <= volume_total


# In[27]:


print(model)


# In[30]:


#Solução do problema
status = model.solve()
print(LpStatus[status])
print(f'Lucro = R${value(model.objective)}')


# In[31]:


for x in var.values():
    if value(x) != 0:
        print(f'{x} = {value(x)}')


# In[ ]:




