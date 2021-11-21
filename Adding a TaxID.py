#!/usr/bin/env python
# coding: utf-8

# In[9]:


import os


# In[10]:


os.getcwd()


# In[291]:


f = open("t1r3_aligned2.fa", "r")
file=f.readlines()


# In[292]:


#Lines = f.readlines()


# In[293]:


#for line in Lines:
for line in file:
#    print (line[0])
    if line[0]==">":
#        print (line)
        species=line.split("[")
        specie=species[1]
#        print (species[1])
        animal="["+specie[0:-1]
        print (animal)
#    if line.startswith(">")
#    print line


# In[295]:


dict_t1r3 = open("t1r3_dict.csv", "r")
file2 = dict_t1r3.readlines()
print (file2)


# In[298]:


d={}
for line in file2:
    line2=line.split(",")
#    print (line2[0][2:-2])
    key=line2[0]
    value=line2[1][:-1]
#    print (line2[1][2:-2])
    if key not in d:
        print (key)
        d[key]=value
print (d)


# 

# In[299]:


f = open("t1r3_aligned2.fa", "r")
f3 = open("t1r3_with_taxid.fa", "w")
file=f.readlines()
#for line in Lines:
for line in file:
#    print (line[0])
    if line[0]==">":
#        print (line)
        species=line.split("[")
        specie=species[1]
#        print(specie)
#        print (species[1])
        animal="["+specie[0:-1]
#        print (animal) 
        if animal in d:
#            print (d[animal])
#            print (line[:-1]+" TaxID: "+d[animal])
#        else:
#            print (line)
            f3.write(line[:-1]+" TaxID="+d[animal])
            f3.write("\n")
    else:
#        print (line)
         f3.write(line)
#            print line+" TaxID: "+value
#            print(key+" TaxID: "+value)
#           print (value)
#            print (key)


# In[177]:


print(f3)


# In[ ]:




