#!/usr/bin/env python
# coding: utf-8

# In[71]:


import csv
from datetime import datetime, timedelta
from pprint import pprint


# In[2]:


sharkfile = r'c:\data\GSAF5.csv'


# In[64]:



with open(sharkfile) as f:
    reader = csv.DictReader(f)
# references columns via headings
    for n in reader:
        #print(n)

    #how we show what in file


# In[74]:


attack_date= []
case = []
country = []
isfatal = []
activity =[]
age = []
gender = []
with open(sharkfile, encoding = None) as f:
    reader = csv.DictReader(f)
# references columns via headings
    for row in reader:
        case.append(row['Case Number'])  #'name from the csv'
        attack_date.append(row['Date'])
        country.append(row['Country'])
        activity.append(row['Activity'])
        age.append(row['Age'])
        gender.append(row['Sex '])
        isfatal.append(row['Fatal (Y/N)'])


# In[75]:


data = zip(attack_dates, case, country, activity, age, gender, isfatal) # make sure same order as data is in using new list


# In[ ]:


cur.execute('truncate table yob.shark')


# In[82]:


import pyodbc
conn = pyodbc.connect('DSN=kubricksql;UID=DE14;PWD=password')
cur= conn.cursor()
s = 'insert into yob.shark (attack_date, case_number,country,activity, age, gender, isfatal) values (?,?,?,?,?,?,?)'


# In[83]:


for d in data:
    try: 
        cur.execute(s,d)
        conn.commit()
    except:
        conn.rollback()


# In[ ]:





# In[ ]:




