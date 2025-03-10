class Uni:
    def __init__(self,name):
        self.name = name
        self.dept = []
    def add_dept(self,dept):
        self.dept.append(dept)
    def show_details(self):
        print(f"Welcome to {self.name}")
        for d in self.dept:
            d.show_details()

class Dept:
    def __init__(self,name,hod):
        self.name = name
        self.hod = hod
        self.prof = []
    def add_prof(self,prof):
        self.prof.append(prof)
        prof.dept = self.name
    def show_details(self):
        print(f"{self.name} Department")
        if self.prof:
            for prof in self.prof:
                print(f"{prof.name}:{prof.subject}")
        else:
            print("No professors assigned yet")


class Prof:
    def __init__(self,name,subject,dept=None):
        self.name = name
        self.subject = subject
        self.dept = dept
    def show_details(self):
        print( f"Name : {self.name}\nSubject : {self.subject}\nDepartment : {self.dept if self.dept else "N/A"}")
    

uni = Uni("Tech University")

# 🔹 Creating departments
dept1 = Dept("Computer Science", "Dr. Smith")
dept2 = Dept("Mathematics", "Dr. Brown")

# 🔹 Adding departments to the university
uni.add_dept(dept1)
uni.add_dept(dept2)

# 🔹 Creating professors
prof1 = Prof("Prof. Alice", "AI")
prof2 = Prof("Prof. Bob", "Cybersecurity")
prof3 = Prof("Prof. Charlie", "Calculus")

# 🔹 Assigning professors to departments
dept1.add_prof(prof1)
dept1.add_prof(prof2)
dept2.add_prof(prof3)

# 🔹 Display university details
uni.show_details()

# 🔹 Show professor details separately
prof1.show_details()
prof2.show_details()
prof3.show_details()

        
        
    

