from datetime import date
class Person:
    def __init__(self,name,country,date_of_birth):
       self.name=name
       self.country=country
       self.date_of_birth=date_of_birth

    def calculate_age(self):
        today= date.today()
        age=today.year-self.date_of_birth.year
        if today<date(today.year,self.date_of_birth.month,self.date_of_birth.day):
            age-=1
        return age


person1=Person("ANIL KUMAR","ONGOLE",date(2006,8,19))

print("calculated age for each person")
print("********************************")
print("Person1:")
print("Name:", person1.name)
print("Country:",person1.country)
print("Date of Birth:",person1.date_of_birth)
print("Age:",person1.calculate_age())
