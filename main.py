class Person:
    def __init__(self, peron_name, year_of_birth: int, ht_inches: int ):
        self.name = peron_name
        self.date_of_birth = year_of_birth
        self.height = ht_inches

    def get_name(self):
        return self.name

    def get_summary(self):
        return f"Name :{self.name}, DOB :{self.date_of_birth} , Height :{self.height if self.height >= 12 else 'u r eligible'}"

    def get_year_of_birth(self):
        return self.date_of_birth


person_list = [Person("ADIB1", 2008, 2),
               Person("ADIB1", 2006,12),
               Person("ADIB1", 2011,11),
               Person("ADIB1", 2009, 32),
               Person("ADIB1", 2006,14),
               Person("ADIB1", 2004, 24)]
for person in person_list:
    if person.get_year_of_birth() is not None and person.get_year_of_birth() >= 2005:
        print(person.get_summary())

class Student(Person):
    def __init__(self,person_name : str, year_of_birth : int,email_id : str, student_id : str,ht_inches : int):
        super().__init__(person_name, year_of_birth,ht_inches)
        self.id = student_id
        self.email = email_id

    def get_summary(self):
        return f"Name :{self.get_name()}, DOB :{self.get_year_of_birth()} StudentID:{self.id}, Email ID : {self.email},Height :{self.height}"


student = Student("ADIB",2005,"sdadff21324","ADIB%%34@gmail.com",12)
print(student.get_summary())