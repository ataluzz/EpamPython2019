"""
Представьте, что вы пишите программу по формированию и выдачи комплексных обедов для сети столовых, которая стала
расширяться и теперь предлагает комплексные обеды для вегетарианцев, детей и любителей китайской кухни.

С помощью паттерна "Абстрактная фабрика" вам необходимо реализовать выдачу комплексного обеда, состоящего из трёх
позиций (первое, второе и напиток).
В файле menu.yml находится меню на каждый день, в котором указаны позиции и их принадлежность к
определенному типу блюд.
"""

import yaml

menu = yaml.load(open("C:/Users/Zlata/Desktop/menu.yml"))
#print(menu)
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays_rus = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

class AbstractLunch:
    def __init__(self, menu):
        self._menu = menu
    
    def first_course(self, weekday):
        raise NotImplementedError()

    def second_course(self, weekday):
        raise NotImplementedError()

    def drink(self, weekday):
        raise NotImplementedError()
        
    def make_lunch(self, weekday):
        print(f"Меню ({weekdays_rus[weekdays.index(weekday)]}):")
        print(f"Первое блюдо: {self.first_course(weekday)}")
        print(f"Второе блюдо: {self.second_course(weekday)}")
        print(f"Напиток: {self.drink(weekday)}")

class VeganLunch(AbstractLunch):
    def first_course(self, weekday):
        return self._menu[weekday]['first_courses']['vegan']
    
    def second_course(self, weekday):
        return self._menu[weekday]['second_courses']['vegan']
    
    def drink(self, weekday):
        return self._menu[weekday]['drinks']['vegan']
    
class ChildLunch(AbstractLunch):
    def first_course(self, weekday):
        return self._menu[weekday]['first_courses']['child']
    
    def second_course(self, weekday):
        return self._menu[weekday]['second_courses']['child']
    
    def drink(self, weekday):
        return self._menu[weekday]['drinks']['child']
    
class ChineseLunch(AbstractLunch):
    def first_course(self, weekday):
        return self._menu[weekday]['first_courses']['chinese']
    
    def second_course(self, weekday):
        return self._menu[weekday]['second_courses']['chinese']
    
    def drink(self, weekday):
        return self._menu[weekday]['drinks']['chinese']

if __name__ == '__main__':
    vegan_menu = VeganLunch(menu)
    child_menu = ChildLunch(menu)
    china_menu = ChineseLunch(menu)

    vegan_menu.make_lunch('Saturday')
    child_menu.make_lunch('Sunday')
    china_menu.make_lunch('Monday') 
