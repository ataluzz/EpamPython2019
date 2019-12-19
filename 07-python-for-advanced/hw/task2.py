"""
Написать свое property c кэшем и таймаутом
полностью повторяет поведение стандартной property за исключением:
    * хранит результат работы метода некоторое время, которое передается
      параметром в инициализацию проперти
    * пересчитывает значение, если таймер истек
"""
import datetime
import time
import uuid

def timer_property(t):
    
    class MyProperty(object):
        
        def __init__(self, fget=None, fset=None, fdel=None, doc=None):
            self.fget = fget
            self.fset = fset
            self.fdel = fdel
            self.time = 0
            self.__doc__ = doc

        def __get__(self, obj, objtype=None):
            if obj is None:
                return self
            if self.fget is None:
                raise AttributeError("can't read attr")
            if datetime.datetime.now() - self.time > datetime.timedelta(seconds = t):
                self.time = datetime.datetime.now()
                self.result = self.fget(obj)
                return self.result
            return self.result

        def __set__(self, obj, value):
            if self.fset is None:
                raise AttributeError("can't set attr")
            self.time = datetime.datetime.today()
            self.result = value

        def __delete__(self, obj):
            if self.fdel is None:
                raise AttributeError("can't del attr")
            self.fdel(obj)
            
        def getter(self, fget):
            return type(self)(fget, self.fset, self.fdel, self.__doc__)
        
        def setter(self, fset):
            return type(self)(self.fget, fset, self.fdel, self.__doc__)
        
        def deleter(self, fdel):
            return type(self)(self.fget, self.fset, fdel, self.__doc__)
    
    return MyProperty


class Message:

    @timer_property(t=5)
    def msg(self):
        self._msg = self.get_message()
        return self._msg

    @msg.setter # reset timer also
    def msg(self, param):
        self._msg = param

    def get_message(self):
        """
        Return random string
        """
        return uuid.uuid4()


if __name__ == '__main__':
    m = Message()
    m.msg = 'hello'
    initial = m.msg
    print(initial is m.msg)
    time.sleep(6)
    print(initial is m.msg)
