from unittest import TestCase
from threefive import ThreeFiveManager

class TestThreeFiveManager(TestCase):

    # testing with default values
    def test_result(self):
        expected=list(["Three",4,"Five"])

        manager=ThreeFiveManager()
        result=manager.get(3,5)
        self.assertListEqual(result,expected)

#testing invalid range
    def test_invalid_range(self):
        expected=list()
        manager=ThreeFiveManager()
        result=manager.get(3,1)
        self.assertListEqual(result,expected)
