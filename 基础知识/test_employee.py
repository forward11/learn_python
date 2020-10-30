import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.new_employee=Employee('james','harden',2333)
    

    def test_give_default_raise(self):
        self.new_employee.give_raise(3000)
        self.assertEqual(self.new_employee.salary,5333)
    
    def test_give_custom_raise(self):
        self.new_employee.give_raise()
        self.assertEqual(self.new_employee.salary,7333)

unittest.main()
    