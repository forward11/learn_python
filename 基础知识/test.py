import unittest

def get_formatted_name(first,last,middle=''):
    """生成整洁的姓名"""
    if middle:
        full_name = first+" "+middle +" " +last
    else:
        full_name = first + " " + last
    return full_name.title()

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name=get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')

    def test_first_last_middle_name(self):
        formatted_name=get_formatted_name('wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')

unittest.main()
