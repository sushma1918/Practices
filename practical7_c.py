# Definig a class student, which contain  subject marks
# math, physics, computer

class Student_Marks:
    def __init__(self,name, sub1, sub2, sub3):
        self.name = name 
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
    
    def getresult(self):
        totalmarks =  self.sub1 +  self.sub2 +  self.sub3
        result = (totalmarks/3) 
        if result >= 33:
            return f"Hi  {self.name}! you are pass "
        else:
            return f" Hi  {self.name} ! you are failed"    
        
    def _str_(self):
        return self.name + " : " + str(self.getresult())
  

# Start Program :
name = input("Enter the name of the student: ")
sub1 = int(input("Enter 1st subject's  marks :  "))
sub2 = int(input("Enter 2nd subject number : "))
sub3 = int(input("Enter 3rd subject number : "))


ob = Student_Marks(name, sub1,sub2,sub3)
print(ob.getresult())

