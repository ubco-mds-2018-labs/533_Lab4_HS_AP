
# coding: utf-8

# In[1]:

import pandas as pd
import unittest
import pkg.modify.apnd as p1
import pkg.query.qry as p4

#df = pd.DataFrame(columns=["eno","ename","age","salary"])
#df = p1.addat(df,[["1265","John",23,50000]])
#data = [["1265","John",23,50000],["4598","Sara",45,85000],["2360","Bob",65,120000],["1839","Julia",21,55000],["7632","Mike",52,150000]]

class TestQry(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('Setup Class')

    
    def setUp(self):
        self.df = pd.DataFrame(columns=["eno","ename","age","salary"])
        self.data = [["1265","John",23,50000],["4598","Sara",45,85000],["2360","Bob",65,120000],["1839","Julia",21,55000],["7632","Mike",52,150000]]
        self.df = p1.addat(self.df,self.data)
        self.count = p4.count(self.df)
        self.agel = 25
        self.ageu = 56
        self.sall = 67000
        self.salu = 100000
        self.eno = '4598'
        self.name = 'Sara'
        self.df2 = p4.fltr(self.df,self.agel,self.ageu,self.sall,self.salu)
        self.count2 = p4.count(self.df2)
        print('Set Up')
    
    
    def test_df_Qry(self):
        
        self.assertEqual(self.count,5)
        self.assertEqual(self.count2,1)
        
        self.assertIsNotNone(self.df)
        self.assertIsNotNone(self.df2)
        
        self.assertTrue(self.agel <= self.df2.iloc[0,2] <= self.ageu)
        self.assertTrue(self.sall <= self.df2.iloc[0,3] <= self.salu)
        
        self.assertFalse(self.agel >= self.df2.iloc[0,2] >= self.ageu)
        self.assertFalse(self.sall >= self.df2.iloc[0,3] >= self.salu)
        
        self.assertEqual(self.df2.iloc[0,0],self.eno)
        self.assertEqual(self.df2.iloc[0,1],self.name)
       
        self.assertNotEqual(self.df2.iloc[0,0],'7632')
        self.assertNotEqual(self.df2.iloc[0,1],'Mike')
        
        
        
    def tearDown(self):
        print('Tear Down')
    
    @classmethod
    def tearDownClass(cls):
        print('Tear Down Class')
        
        
unittest.main(argv=[''], verbosity=2, exit=False)


# In[ ]:



