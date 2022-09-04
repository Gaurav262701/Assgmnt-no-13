#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# In[3]:


#Answer no 1
#Write a program that calculates and prints the value according to the given formula:
c = 50 
h = 30
value = []
items=[x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
    
print(','.join(value))


# In[5]:


#Answer no 2
#Write a program which takes 2 digits
row_num = int(input("input number of rows:"))
col_num = int(input("input number of colum:"))
multi_list = [[0 for col in range(col_num)] for now in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]=row*col
        
print(multi_list)


# In[6]:


#Answer no 3
#Write a program that accepts a comma separated sequence of words as input and prints the
#words in a comma-separated sequence after sorting them alphabetically.
items = input("input comma searated sequence of words")
words = [word for word in items.split(',')]
print(",".join(sorted(list(set(words)))))


# In[7]:


#Answer no 4
#Write a program that accepts a sequence of whitespace separated words as input and prints
#the words after removing all duplicate words and sorting them alphanumerically.
s = input()
words = [word for word in s.split(" ")]
print(" ".join(sorted(list(set(words)))))


# In[8]:


#Answer no 5
#Write a program that accepts a sentence and calculate the number of letters and digits.
s = input()
d = {"DIGITS":0,'LETTERS':0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
    
print("LETTERS",d["LETTERS"])
print("DIGITS",d["DIGITS"])


# In[9]:


import re


# In[12]:


#Answer no 6

value = []
items = [x for x in input().split(',')]
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    value.append(p)
print(",".join(value))


# In[ ]:




