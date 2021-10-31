#!/usr/bin/env python
# coding: utf-8

# #### Sorting of First CSV

# In[1]:


import pandas as pd
csvData = pd.read_csv('/Users/prernakamboj/Downloads/data/QueryResults1.csv')
csvData.sort_values(["ViewCount"], ascending=[False], inplace=True)
csvData.to_csv('/Users/prernakamboj/Downloads/data/QueryResults1.csv')


# #### Sorting of Second CSV

# In[3]:


import pandas as pd
csvData1 = pd.read_csv('/Users/prernakamboj/Downloads/data/QueryResults2.csv')
csvData1.sort_values(["ViewCount"], ascending=[False], inplace=True)
csvData1.to_csv('/Users/prernakamboj/Downloads/data/QueryResults2.csv')


# #### Sorting of Third CSV

# In[5]:


import pandas as pd
csvData2 = pd.read_csv('/Users/prernakamboj/Downloads/data/QueryResults3.csv')
csvData2.sort_values(["ViewCount"], ascending=[False], inplace=True)
csvData2.to_csv('/Users/prernakamboj/Downloads/data/QueryResults3.csv')


# #### Sorting of Fourth CSV

# In[7]:


import pandas as pd
csvData3 = pd.read_csv('/Users/prernakamboj/Downloads/data/QueryResults4.csv')
csvData3.sort_values(["ViewCount"], ascending=[False], inplace=True)
csvData3.to_csv('/Users/prernakamboj/Downloads/data/QueryResults4.csv')


# #### Sorting of Fifth CSV

# In[ ]:


import pandas as pd
csvData = pd.read_csv('/Users/prernakamboj/Downloads/data/QueryResults5.csv')
csvData.sort_values(["ViewCount"], ascending=[False], inplace=True)
csvData.drop(csvData.tail(5087).index,inplace=True)
csvData.to_csv('/Users/prernakamboj/Downloads/data/QueryResults5.csv')


# #### Merging of all 5 csv files

# In[34]:


import pandas as pd
from glob import glob
Querydata_files = sorted(glob('/Users/prernakamboj/Downloads/data/QueryResults*.csv'))
merged_file = pd.concat(pd.read_csv(Querydatafiles)
                        for Querydatafiles in Querydata_files)
merged_file.to_csv('/Users/prernakamboj/Downloads/data/Merged.csv')


# In[35]:


len(merged_file)


# #### Checking for the dupliacte value

# In[ ]:


Merged_file.drop_duplicates()


# #### Renaming of the Columns

# In[ ]:


merged_file.columns['Id','PostTypeId','AcceptedAnswerId','ParentId','CreationDate','DeletionDate','Score','ViewCount','Body','OwnerUserId','OwnerDisplayName','LastEditorUserId','LastEditorDisplayName','LastEditDate','LastActivityDate','Title','AnswerCount','CommentCount','FavoriteCount','ClosedDate','CommunityOwnedDate','ContentLicense']
merged_file


# #### Removal of unwanted columns

# In[53]:


merged_file = pd.read_csv('/Users/prernakamboj/Downloads/data/Merged.csv')
merged_file = merged_file.drop(merged_file.columns[[0, 1]], axis=1)
merged_file


# #### Missing values or empty values replaced with 0

# In[54]:


merged_file.fillna(0)

