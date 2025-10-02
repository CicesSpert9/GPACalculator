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
        return round(GPA, 2) 
    
    
    def __str__(self):
        
        return print("Student: {} (ID: {}) GPA: {}".format(str(self.name), str(self.studentid), str(self.calculate_GPA)))
         

name = input(f"What is your student name?")
studentid = input(f"What is your student ID?")
student = Student(name, studentid)

while True:
    course = input(f"What course are you taking?")
    credits = input(f"What are your credits in {course}?")
    grades = input(f"What is your grade in {course}")
    if course.lower() == "done":
        


        






     
    
