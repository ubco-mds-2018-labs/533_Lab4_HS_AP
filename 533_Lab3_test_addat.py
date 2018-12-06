
# coding: utf-8

# In[1]:

import pandas as pd
import unittest
import pkg.modify.apnd as p1

#df = pd.DataFrame(columns=["eno","ename","age","salary"])
#df = p1.addat(df,[["1265","John",23,50000]])
#data = [["1265","John",23,50000],["4598","Sara",45,85000],["2360","Bob",65,120000],["1839","Julia",21,55000],["7632","Mike",52,150000]]

class TestAdd(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('Setup Class')

    
    def setUp(self):
        self.df = pd.DataFrame(columns=["eno","ename","age","salary"])
        self.df = p1.addat(self.df,[["1265","John",23,50000]])
        self.data = [["1265","John",23,50000],["4598","Sara",45,85000],["2360","Bob",65,120000],["1839","Julia",21,55000],["7632","Mike",52,150000]]
        print('Set Up')
    
    
    def test_df_Add(self):
        
        self.assertEqual(self.df.iloc[0,0],'1265')
        self.assertEqual(self.df.iloc[0,1],'John')
        self.assertEqual(self.df.iloc[0,2],23)
        self.assertEqual(self.df.iloc[0,3],50000)
        
        self.assertNotEqual(self.df.iloc[0,0],'4598')
        self.assertNotEqual(self.df.iloc[0,1],'Sara')
        self.assertNotEqual(self.df.iloc[0,2],45)
        self.assertNotEqual(self.df.iloc[0,3],85000)
        
        
        self.assertIn(list(self.df.loc[0]),self.data)
        
        self.assertNotIn([["5699","Harry",78,123000]],self.data)
        
        self.assertIsNotNone(self.df)
        
    def tearDown(self):
        print('Tear Down')
    
    @classmethod
    def tearDownClass(cls):
        print('Tear Down Class')
        
        
unittest.main(argv=[''], verbosity=2, exit=False)


# In[ ]:




# In[ ]:



