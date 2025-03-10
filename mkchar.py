class Employee:
    def __init__(self,name,age,position=None,salary=None ):
        self.name =name
        self.age = age
        self.position =position or "Intern"
        self.salary = salary or 0

    def display_info(self):
        return f"Name: {self.name}\nAge: {self.age}\nPosition: {self.position}\nSalary: {self.salary}"
    
    def update_salary(self,amount):
        if amount > 0:
            self.salary += amount
            return "Salary update successful"
        else:
            return "Please enter valid value"
        
    def promote(self,new_position,salary_increase=None):
        self.position = new_position
        if salary_increase:
            self.salary += salary_increase
        return f"{self.name} has just been promoted to {new_position} with a salary increase of {salary_increase}!"
    
employee1 = Employee("Evame", 22, "IT Specialist", 500)
employee2 = Employee("Elvis", 22, "IT Specialist", 600)
print(employee1.display_info())
print(employee2.display_info())
print(employee1.promote("IT Manager", 500))
print(employee1.display_info())
print(employee2.display_info())



        
    
         
        