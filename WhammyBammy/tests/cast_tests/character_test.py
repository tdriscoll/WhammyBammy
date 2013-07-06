import unittest
from common.coordinate import ORIGIN
from cast.character import Character

class CharacterTest(unittest.TestCase):

    def test_create_protagonist(self):
        p = Character(ORIGIN)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()