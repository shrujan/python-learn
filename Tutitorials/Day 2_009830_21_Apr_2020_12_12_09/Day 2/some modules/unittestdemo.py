import unittest

#def my_func(a,'ttest_ex.pyb'):
def my_func(a,b):
    return a * b

class TestME(unittest.TestCase):  # TestME is a user defined class
    def setup(self):
        pass
    def testnum(self):              #testnum is user defined method
        self.assertEqual(my_func(3,4),12)

    def teststr(self):
        self.assertEqual(my_func('a',3),'aaa')

if __name__ == '__main__':
        unittest.main()  #transefers the control to TestME class
