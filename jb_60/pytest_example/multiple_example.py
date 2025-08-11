import unittest


class multipleExample(unittest.TestCase):

    def test_add(self):
        print("testing summery")
        num1= 1
        num2= 2
        assert num1+num2 ==3, "The summery of 1 and 2 is not 3"

    def test_minus(self):
        print("testing diff")
        num1 =4
        num2 =1
        assert num1-num2 ==3, "The diff of 4 and 1 is not 3"

    def test_multiple_with_erro(self):
        num1 =3
        num2 =2
        assert num1*num2 ==5, "The result of multiple action is not as expected"