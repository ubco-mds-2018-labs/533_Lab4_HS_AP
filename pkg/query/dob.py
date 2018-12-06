
# coding: utf-8

# In[ ]:

class emp:    # Super class, any Vehicle
    def __init__(self,eno): # initialize make,model and year
        
        self.eno = eno
        
        #print("Initialized Vehicle: {} ".format(self.make))

    def display(self): # display Vehicle details
        print("Employee No: {}".format(self.eno))


class dob(emp): # Truck subclass, represents a truck
    
    def __init__(self,eno,dob):
        emp.__init__(self,eno)
        self.dob = dob
        
        
    def display(self):
        emp.display(self)
        print("Date of Birth: {}".format(self.dob))        
        
 
        

