import unittest
import notes

class Test(unittest.TestCase):

    def test_finder(self):
        result = notes.finder([1,2,3,3,4,5,6,7],[3,7,2,1,4,6,8,9])
        print(f'Expected [5], got {result}')
        self.assertEqual(result,[5])

    def test_large_cont_sum(self):
        result = notes.large_cont_sum([1,2,-1,3,4,10,10,-10,-1])
        print(f'Expected 29, got {result}')
        self.assertEqual(result,29)

if __name__ == '__main__':
    unittest.main()