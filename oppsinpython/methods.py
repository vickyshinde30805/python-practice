class student:
    #class attributes are same for all object ex
    collage_name="NCER"

    def __init__(self,fullname):
        self.name=fullname #this is instance attribute it is diffrent for each object and defined by self keyword

    def hello(self):
        print ("hello",self.name)    
        
       

s1=student("Vicky")#creat the class object
s1.hello()