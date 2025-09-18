class Student:
    def __init__(self, name, studentid):
        self.name = name
        self.studentid = studentid
        self.courses = {}
    def course(self, name, grades, credits):
        self.courses[name] = (credits, grades)
    def calculate_GPA(self):
        for credits, grades in self.courses.values():
            total_points += credits * grades
            total_credits += credits 
            GPA = total_points/ total_credits
    def __str__(self):
         print("Student: {} (ID: {}) GPA: {}".format(str(self.name), str(self.studentid), str(self.calculate_GPA)))




 name = input(f"What course are you taking?")
        credits = input(f"What are your credits in {self.name}?")
        grades = input(f"What is your grade in {self.name}")






     
    
