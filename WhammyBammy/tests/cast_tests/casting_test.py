import unittest
from common.coordinate import ORIGIN
from cast.casting import Casting
from cast.character import Character


class CastingTest(unittest.TestCase):


    def test_can_create_protagonist(self):
        actual = Casting.create_protagonist(ORIGIN)
        expected = Character(location= ORIGIN)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()