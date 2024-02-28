import main 
import unittest

A=main.Block2(0)
A.getDict()
def checkBlock(number):
    return main.getBlock(number)

class TestCalculaMedia(unittest.TestCase):
    def test_1(self):
        number=0
        output = checkBlock(number)["number"]
        self.assertEqual(len(checkBlock(number)['transactions'] ),0)
        self.assertEqual(len(checkBlock(number)['uncles']),0)
        self.assertEqual(output, 0)
        number=10000000
        self.assertEqual(len(checkBlock(number)['transactions'] ),20)
        self.assertEqual(len(checkBlock(number)['uncles']),0)
        self.assertEqual(output, 0)

    def test_2(self):
        output = main.getBlock(10000000)["number"]
        self.assertEqual(output, 10000000)

if __name__ == '__main__':
    unittest.main()






