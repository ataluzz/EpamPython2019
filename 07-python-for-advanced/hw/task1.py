"""

Реализовать такой метакласс, что экземпляры класса созданного с помощью него
будут удовлетворять следующим требованиям:

* объекты созданные с одинаковыми аттрибутами будут одним и тем же объектом
* объекты созданные с разными аттрибутами будут разными объектами
* у любого объекта есть мозможность получить доступ к другим объектам
    того же класса


>>> unit1 = SiamObj('1', '2', a=1)
>>> unit2 = SiamObj('1', '2', a=1)
>>> unit1 is unit2
True
>>> unit3 = SiamObj('2', '2', a=1)
>>> unit3.connect('1', '2', 1).a = 2
>>> unit2.a == 2
True
>>> pool = unit3.pool
>>> print(len(pool))
2
>>> del unit3
>>> print(len(pool))
1

"""

class MetaSingleton(type):
    
    _list_of_inst = []
    _instances = {}
    _attributes = {}
    
    def __call__(cls, *args, **kwargs):
                
        def get_key(d, value):
            for k, v in d.items():
                if v == value:
                    return k
                        
        def new_del(instance): # i need help
            if instance in cls._list_of_inst:
                index = cls._list_of_inst.index(instance)
                del cls._list_of_inst[index]

            if instance in cls._attributes.keys():
                del cls._attributes[instance]
                
            if instance in cls._instances[cls]:
                ind = cls._instances[cls].index(instance)
                del cls._instances[cls][ind]
            
        def connect(*args, **kwargs):
            attrs = (args + tuple(kwargs.values()))
            a = get_key(cls._attributes, attrs)
            return a
        
        for key in cls._attributes:
                if cls._attributes[key] == (args + tuple(kwargs.values())):
                    cls._instances[cls] = get_key(cls._attributes, (args + tuple(kwargs.values())))
                    return cls._instances[cls]
        instance = super(MetaSingleton, cls).__call__(*args, **kwargs)
        cls._list_of_inst.append(instance)
        cls._instances[cls] = cls._list_of_inst
        cls._attributes[instance] = (args + tuple(kwargs.values()))
        cls.__del__ = new_del
        instance.connect = connect
        instance.pool = cls._attributes
        return instance
    
        
    
class SiamObj(metaclass = MetaSingleton):
    
    def __new__(cls, *args, **kwargs):
        return super(SiamObj, cls).__new__(cls)
    
    def __init__(self, *args, **kwargs):
        super(SiamObj, self).__init__()
        

if __name__ == '__main__':
    unit1 = SiamObj('2', '2', a=1)
    unit2 = SiamObj('2', '2', a=1)
    print(unit1)
    print(unit2)
    print(unit1 is unit2)
    unit3 = SiamObj('7', '2', a=1)
    unit4 = SiamObj('3', '1', a=9)
    print(unit4)
    print(unit3)
    print(unit2 is unit3)
    unit3.connect('2', '2', 1).a = 5
    print(unit2.a == 5)
    pool = unit4.pool
    print(len(pool))
    del unit3
    print(len(pool))
