"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    counter = 0
    class NewCls(object):
        def __init__(self, *args, **kwargs):
            self.instance = cls(*args, **kwargs)
            nonlocal counter
            counter += 1
        
        @classmethod
        def get_created_instances(self):
            nonlocal counter
            return counter
        
        @classmethod
        def reset_instances_counter(self):
            nonlocal counter
            answer = counter
            counter = 0
            return answer
    return NewCls


@instances_counter
class User:
    pass


if __name__ == '__main__':

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
