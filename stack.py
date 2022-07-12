class EmployeeDB():
    def __init__(self, emp_id, emp_name, emp_age):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_age = emp_age

    def findAge(self):
    #Returns emp_age attribute of the argued object
        return self.emp_age



#Creating 4 objects of EmployeeDB class
emp1 = EmployeeDB(emp_id=1001, emp_name="Raj1", emp_age=25)
emp2 = EmployeeDB(emp_id=1002, emp_name="Raj2", emp_age=26)
emp3 = EmployeeDB(emp_id=1003, emp_name="Raj3", emp_age=27)
emp4 = EmployeeDB(emp_id=1004, emp_name="Raj4", emp_age=28)

#Method which takes a scecific emploee's ID and returns AGE
def findAgeOf_emp_id(id):
    if emp1.emp_id == id:
        print(id)
        return emp1.findAge()

    elif emp2.emp_id == id:
        print(id)
        return emp2.findAge()

    elif emp3.emp_id == id:
        print(id)
        return emp3.findAge()

    elif emp4.emp_id == id:
        print(id)
        return emp4.findAge()
    else :
        return "no employee found"


#Usage
print (findAgeOf_emp_id(1003))