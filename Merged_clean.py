#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import re

def main():
    data_csv = pd.read_csv('/Users/prernakamboj/Downloads/data/Merged.csv', usecols=['Id', 'Score', 'Body', 'OwnerUserId', 'Title', 'Tags'])
    data_dict = data_csv.to_dict()

    count = len(data_dict['Id'])


    for i in range(count):
        data_dict['Body'][i] =  re.sub(r',+', '', data_dict['Body'][i])
        data_dict['Title'][i] = re.sub(r',+', '', data_dict['Title'][i])
        data_dict['Tags'][i] =  re.sub(r',+', '', data_dict['Tags'][i])

        data_dict['Body'][i] =  re.sub(r'(  )+', '', data_dict['Body'][i])
        data_dict['Title'][i] = re.sub(r'(  )+', '', data_dict['Title'][i])
        data_dict['Tags'][i] =  re.sub(r'(  )+', '', data_dict['Tags'][i])

        data_dict['Body'][i] =  re.sub(r'\n+', '', data_dict['Body'][i])
        data_dict['Title'][i] = re.sub(r'\n+', '', data_dict['Title'][i])
        data_dict['Tags'][i] =  re.sub(r'\n+', '', data_dict['Tags'][i])


    pd.DataFrame.from_dict(data_dict).to_csv('/Users/prernakamboj/Downloads/data/Merged_Cleaned.csv', index = False)



if __name__ == "__main__":
    #main()

