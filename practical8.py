'''
Experiment 8
Write a python program to implement Inheritance using different levels.
'''

class Collage:
   def __init__(self,collage_name):
    self.collage_name = collage_name
   
   def get_collage_name(self):
     return self.collage_name

class Branch(Collage):
   def __init__(self,collage_name,branch_name):
     Collage.__init__(self,collage_name)
     self.branch_name = branch_name

   def get_branch_name(self):
     return self.branch_name

class Student(Branch):
   def __init__(self,collage_name,branch_name,student_name):
        Branch.__init__(self,collage_name,branch_name)
        self.student_name = student_name

   def get_student_name(self):
     return self.student_name


# Create a object of Student class
s_object = Student("MMMUT","IT","Sushma Sharma")
print("Collage name : ",s_object.get_collage_name())# get from Collage class
print("Branch name  : ",s_object.get_branch_name()) # get from Branch class
print("Student Name : ", s_object.get_student_name())# get from Student class
