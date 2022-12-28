'''
Experiment 11
(A) Write a python program to create CSV file and store empno,name,salary and search any
empno and display name,salary and if not found appropriate message.

'''

import csv

def add_record_in_file():
    file = open('data.csv','w',newline='')
    f_object = csv.writer(file)
    
    n=int(input("Enter the no.of employees:"))
    for i in range(n):
       emp_id=int(input("Enter the employee number:"))
       emp_name=input("Enter the employee name:")
       emp_salary=int(input("Enter the salary:"))
       f_object.writerow([emp_id,emp_name,emp_salary])

    file.close()

    
def seach_record():
    file = open('data.csv','r')
    f_object = csv.reader(file)
    emp_id = int(input("Enter the employee number to be searched:"))
    for i in f_object:
       if int(i[0])==emp_id:
           print("\n_____________Record found___________\n")
           print("Name:",i[1])
           print("Salary",i[2])
           break
       else:
           print("Record not found")
           break
    file.close()

if __name__ == "__main__":
    while True:
        a = int(input("\n1 : Add new record \n2 : Search record \n0 : Close appliction\n"))
        if a == 1:
            add_record_in_file()
        elif a == 2:
            seach_record()
        elif a == 0  :
            break
        else:
            print("Please select 1,2 or 0 option\n")      
