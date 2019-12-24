"""
Используя паттерн "Декоратор" реализуйте возможность дополнительно добавлять к кофе
    маршмеллоу, взбитые сливки и сироп, а затем вычислить итоговую стоимость напитка.
"""

class Component: 
    def get_cost(self):
        raise NotImplementedError("Override get_cost method")

class ComponentDecorator(Component):
    def __init__(self, added_stuff):
        self.added_stuff = added_stuff
        
        
class BaseCoffee(Component):
    def get_cost(self):
        return 90

        
class Whip(ComponentDecorator):
        
    def get_cost(self):
        print("You added whipped cream. It'll cost you 30")
        return self.added_stuff.get_cost() + 30

class Marshmallow(ComponentDecorator):
        
    def get_cost(self):
        print("You added marshmallow. It'll cost you 10")
        return self.added_stuff.get_cost() + 10
    
class Syrup(ComponentDecorator):
        
    def get_cost(self):
        print("You added syrup. It'll cost you 20")
        return self.added_stuff.get_cost() + 20
        

if __name__ == "__main__":
    coffee = BaseCoffee()
    coffee = Whip(coffee)
    coffee = Marshmallow(coffee)
    coffee = Syrup(coffee)
    print("Итоговая стоимость за кофе: {}".format(str(coffee.get_cost())))
