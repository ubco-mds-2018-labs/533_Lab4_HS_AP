
# coding: utf-8

# In[1]:

import pandas as pd
import unittest
import pkg.query.dob as p3

class TestDOB(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('Setup Class')

    
    def setUp(self):
        
        self.empl = p3.dob("2360","08/18/1996")
        print('Set Up')
    
    
    def test_dob(self):
        
        self.assertEqual(self.empl.eno,"2360") 
        self.assertEqual(self.empl.dob,"08/18/1996")
        
        self.assertIsInstance(self.empl,p3.emp)# emp is a class in the package module dob.py
        self.assertIsInstance(self.empl,p3.dob)# dob is a class in the package module dob.py
        
        
    def tearDown(self):
        print('Tear Down')
    
    @classmethod
    def tearDownClass(cls):
        print('Tear Down Class')
        
        
unittest.main(argv=[''], verbosity=2, exit=False)


# In[ ]:



