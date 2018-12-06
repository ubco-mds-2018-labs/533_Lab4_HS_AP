
# coding: utf-8

# In[ ]:

import pandas as pd

    
def count(df):
    
    try :
        if len(df) != 0 :
            return (len(df)) 
    except : 
        print("Data Frame is empty")
    
def fltr(df,agel,ageu,sall,salu):
    
    try :
        if len(df) != 0 :
            return df[(df.age > int(agel)) & (df.age < int(ageu)) & (df.salary > int(sall)) & (df.salary < int(salu))]
        else : 
            print("Data Frame is empty")
    except : 
        print("Please verify parameters being transfered")

