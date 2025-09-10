class Student:
    def __init__(self, name, studentid):
        self.name = name
        self.studentid = studentid
        self.courses = {}
    def course(self, name, grades, credits):
        self.courses[name] = (credits, grades)
        name = input(f"What course are you taking?")
        credits = input(f"What are your credits in {self.name}?")
        grades = input(f"What is your grade in {self.name}")



     
    
