
# coding: utf-8

# In[ ]:

import pandas as pd

def deldat(df,data):
    
    try : 
        
        if data != None :
            
            
            for i in range(0,len(df)):
                
                if df.loc[i,"eno"] == data:
                    
                    print("Employee exists")
                    df = df.drop(df.index[i])
                    return df.reset_index(drop=True)
        
            print("Employee does not exist")
            return df
    
    except : 
        
        print("Error : No data provided to delete from the data frame")

