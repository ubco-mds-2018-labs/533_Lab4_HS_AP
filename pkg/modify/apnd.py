
# coding: utf-8

# In[ ]:

import pandas as pd

def addat(df,data):
    
    try : 
        
        if data != None :
            
            for i in range(0,len(df)):
                
                if df.loc[i,"eno"] == data[0]:
                    
                    print("Employee already exists")
                    return df 
    
        tmp = pd.DataFrame(data, columns=["eno","ename","age","salary"])
        df = df.append(tmp, ignore_index=True)
        return df
    
    except : 
        
        print("Error : No data provided to append in the data frame")

