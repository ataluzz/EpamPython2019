"""
С помощью паттерна "Цепочка обязанностей" составьте список покупок для выпечки блинов.
Необходимо осмотреть холодильник и поочередно проверить, есть ли у нас необходимые ингридиенты:
    2 яйца
    300 грамм муки
    0.5 л молока
    100 грамм сахара
    10 мл подсолнечного масла
    120 грамм сливочного масла

В итоге мы должны получить список недостающих ингридиентов.
"""

class ListOfIngredients:
    _next_handler = None
        
    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)

    
class EggsHandler(ListOfIngredients):
 
    def handle(self, request):
        if request['eggs'] < 2:
            q = 2 - request['eggs']
            print(f'Яйца, {q} шт.')
        return super().handle(request)
        
        
class FlourHandler(ListOfIngredients):
    def handle(self, request):
        if request['flour'] < 300:
            q = 300 - request['flour']
            print(f'Мука, {q} грамм')
        return super().handle(request)

    
class MilkHandler(ListOfIngredients):
    def handle(self, request):
        if request['milk'] < 0.5:
            q = 0.5 - request['milk']
            print('Молоко, {q} литра')
        else:
            return super().handle(request)

        
class SugarHandler(ListOfIngredients):
    def handle(self, request):
        if request['sugar'] < 100:
            q = 100 - request['sugar']
            print(f'Сахар, {q} грамм')
        return super().handle(request)
        
class SunflowerOilHandler(ListOfIngredients):
    def handle(self, request):
        if request['sfoil'] < 10:
            q = 10 - request['sfoil']
            print(f'Подсолнечное масло, {q} мл')
        return super().handle(request)

    
class ButterHandler(ListOfIngredients):
    def handle(self, request):
        if request['butter'] < 120:
            q = 120 - request['butter']
            print(f'Сливочное масло, {q} грамм')
        return super().handle(request)

curr_products = {'eggs': 3, 'flour': 200, 'milk': 0.7, 'sugar': 50, 'sfoil': 10, 'butter': 20}

eggs = EggsHandler()
flour = FlourHandler()
milk = MilkHandler()
sugar = SugarHandler()
sfoil = SunflowerOilHandler()
butter = ButterHandler()
eggs.set_next(flour).set_next(milk).set_next(sugar).set_next(sfoil).set_next(butter)
eggs.handle(curr_products)
