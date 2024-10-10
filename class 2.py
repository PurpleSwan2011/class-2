class student:
    grade = 8
    name = "Saima"
    
    def introduction(self):
        print("Hi I am a student")
        
    def details(self):
        print("My name is", self.name)
        print("I study in grade 8", self.grade)
    
ob = student()
ob.introduction()
ob.details()