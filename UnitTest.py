from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.testCases = {
            1: {'intervals': [[5,10],[6,8],[1,5],[2,3],[1,10]], 'output': 3},
            2: {'intervals': [[1,3],[5,6],[8,10],[11,13]], 'output': 1}
        }
        self.obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        intervals, output = self.testCases[1].values()
        result = self.obj.minGroups(intervals = intervals)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case2(self):
        intervals, output = self.testCases[2].values()
        result = self.obj.minGroups(intervals = intervals)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()