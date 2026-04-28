class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=student("vicky",20)
del s1.age
print(s1.name) # Output: vicky

    