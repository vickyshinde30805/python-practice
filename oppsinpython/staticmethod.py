class student:
    #class attributes are same for all object ex
    collage_name="NCER"

    def __init__(self,fullname):
        self.name=fullname #this is instance attribute it is diffrent for each object and defined by self keyword


    @staticmethod  #decorator 

    def hello1():# static method do not creat the object of class and do not take self as parameter
        print ("welcome to collage")

    def hello(self):
        print ("hello",self.name)    
        
       

s1=student("Vicky")#creat the class object
student.hello1()
s1.hello()
