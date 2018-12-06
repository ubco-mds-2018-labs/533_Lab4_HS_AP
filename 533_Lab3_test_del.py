
# coding: utf-8

# In[1]:

import pandas as pd

import pkg.modify.apnd as p1
import pkg.modify.dlt as p2
import unittest





class TestAdd(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('Setup Class')

    
    def setUp(self):
        self.df = pd.DataFrame(columns=["eno","ename","age","salary"])
        
        self.data = [["1265","John",23,50000],["2360","Bob",65,120000]]
        self.df = p1.addat(self.df,self.data)
        #print(self.df)
        print('Set Up')
        self.data2='2360'
        self.df2 = p2.deldat(self.df,self.data2)
        
    
    def test_df_Add(self):
     
        
        
        #self.assertIn(list(self.df.loc[0]),self.data)
        
        self.assertNotIn([["2360","Bob",65,120000]],list(self.df2.loc[0]))
        
        
        self.assertEqual(self.df2.iloc[0,0],'1265')
        self.assertEqual(self.df2.iloc[0,1],'John')
        self.assertEqual(self.df2.iloc[0,2],23)
        self.assertEqual(self.df2.iloc[0,3],50000)
        
        self.assertIsNotNone(self.df)
        self.assertIsNotNone(self.df2)
        
        self.assertTrue(len(self.df2)<len(self.df))
        
        self.assertFalse(len(self.df2)>len(self.df))
        
        
        
        
        
        
        
        
        
        
        #self.assertIsNotNone(self.df)
        
    def tearDown(self):
        print('Tear Down')
    
    @classmethod
    def tearDownClass(cls):
        print('Tear Down Class')
        
        
unittest.main(argv=[''], verbosity=2, exit=False)
    


# In[ ]:



