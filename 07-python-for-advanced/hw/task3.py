"""
Написать тесты(pytest or unittest) к предыдущим 2 заданиям, запустив которые, я бы смог бы проверить их корректность
Обязательно проверить всю критическую функциональность
"""
import unittest
from task1 import SiamObj
from task2 import Message
import time
import sys

class TestTask1(unittest.TestCase):
    
    def test_same_instance(self):
        unit1 = SiamObj('1', '2', a=1)
        unit2 = SiamObj('1', '2', a=1)
        self.assertEqual(unit1, unit2, 'Must be the same instance')
        
    def test_not_same_instance(self):
        unit1 = SiamObj('1', '2', a=1)
        unit3 = SiamObj('2', '2', a=1)
        self.assertNotEqual(unit1, unit3, 'Must not be the same instance')
        
    def test_connect(self):
        unit1 = SiamObj('1', '2', a=1)
        unit2 = SiamObj('1', '2', a=1)
        unit3 = SiamObj('2', '2', a=1)
        unit3.connect('1', '2', 1).a = 2
        self.assertEqual(2, unit1.a, 'Attribute of instance is not assigned to value')
        self.assertEqual(2, unit2.a, 'Attribute of instance is not assigned to value')
        
    def test_delete(self):
        unit1 = SiamObj('1', '2', a=1)
        unit2 = SiamObj('1', '2', a=1)
        unit3 = SiamObj('2', '2', a=1)
        pool = unit3.pool
        self.assertEqual(2, len(pool), 'Wrong number of instances of SiamObj class')
        del unit3
        self.assertEqual(1, len(pool), "Delete didn't work")
        

class TestTask2(unittest.TestCase):
    
    def test_for_same_msg(self):
        m = Message()
        initial = m.msg
        self.assertEqual(m.msg, initial, 'Not the same msg')
        
    def test_for_msg_with_delay(self):
        m = Message()
        initial = m.msg
        time.sleep(6)
        self.assertNotEqual(m.msg, initial, 'Must not be the same message (timer error)')
        
    def test_setter(self):
        m = Message()
        m.msg = 'hello'
        initial = m.msg
        self.assertEqual(m.msg, initial, "Setter didn't assert new value to msg")
        
    def test_setter_with_delay(self):
        m = Message()
        m.msg = 'hello'
        initial = m.msg
        time.sleep(6)
        self.assertNotEqual(m.msg, initial, 'Must not be the same message (timer error)')
        

#suite = unittest.TestLoader().loadTestsFromTestCase(TestTask1)
#suite2 = unittest.TestLoader().loadTestsFromTestCase(TestTask2)
#unittest.TextTestRunner(verbosity=3,stream=sys.stderr).run(suite)
#unittest.TextTestRunner(verbosity=3,stream=sys.stderr).run(suite2)
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=3)
