import datetime

class Homework:
    
    def __init__(self, text, days):
        self.text = text
        self.deadline = datetime.timedelta(days)
        self.created = datetime.datetime.today()
    
    def is_active(self):
        if datetime.datetime.today() >= self.deadline + self.created:
            return False
        else:
            return True
            
class Student:
    
    def __init__(self, first_name, last_name):
        self.last_name = last_name
        self.first_name = first_name
    
    def do_homework(self, homew):
        if homew.is_active():
            return homew
        else:
            print("You are late")
            
class Teacher:
        
    def __init__(self, first_name, last_name):
        self.last_name = last_name
        self.first_name = first_name
    
    def create_homework(self, text, deadline):
        hw = Homework(text, deadline)
        return hw


if __name__ == '__main__':
    teacher = Teacher('Daniil', 'Shadrin')
    student = Student('Roman', 'Petrov')
    print(teacher.last_name)  # Shadrin
    print(student.first_name)  # Roman

    expired_homework = teacher.create_homework('Learn functions', 0)
    print(expired_homework.created)  # Example: 2019-05-26 16:44:30.688762
    print(expired_homework.deadline)  # 0:00:00
    print(expired_homework.text)  # 'Learn functions'

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    print(oop_homework.deadline)  # 5 days, 0:00:00

    print(student.do_homework(oop_homework))
    print(student.do_homework(expired_homework))  # You are late
