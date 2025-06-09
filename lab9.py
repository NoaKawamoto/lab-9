import heapq
import unittest

class KthLargestFinder:
    def solve_finder(self, numbers: list[int], k: int) -> int:
        unique_numbers = set(numbers)

        if k <= 0 or len(unique_numbers) < k:
            return -1

        min_heap = []

        for num in unique_numbers:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                heapq.heappushpop(min_heap, num)

        return min_heap[0]

class TestKthLargestFinder(unittest.TestCase):
    def setUp(self):
        self.finder = KthLargestFinder()

    def test_example(self):
        self.assertEqual(self.finder.solve_finder([10, 3, 8, 15, 7], 3), 8)

    def test_elements(self):
        self.assertEqual(self.finder.solve_finder([30, 20, 10, 40], 4), 10)

    def test_desc(self):
        self.assertEqual(self.finder.solve_finder([90, 80, 70, 60], 2), 80)

    def test_asc(self):
        self.assertEqual(self.finder.solve_finder([5, 10, 15, 20], 1), 20)

    def test_duplicate(self):
        self.assertEqual(self.finder.solve_finder([50, 50, 50, 50], 2), -1)

    def test_negatives(self):
        self.assertEqual(self.finder.solve_finder([-2, -5, 0, -8, 3, 3], 3), -2)

    def test_k_equals_one(self):
        self.assertEqual(self.finder.solve_finder([99, 42, 75, 64], 1), 99)

    def test_large_k(self):
        self.assertEqual(self.finder.solve_finder([11, 22, 22, 33], 4), -1)

    def test_one_element(self):
        self.assertEqual(self.finder.solve_finder([123], 1), 123)

    def test_one_element_k(self):
        self.assertEqual(self.finder.solve_finder([123], 2), -1)

    def test_empty(self):
        self.assertEqual(self.finder.solve_finder([], 1), -1)

    def test_negative_k(self):
        self.assertEqual(self.finder.solve_finder([6, 7, 8], -2), -1)

    def test_negative_v(self):
        self.assertEqual(self.finder.solve_finder([-11, -7, -30, -2], 2), -7)

    def test_negative(self):
        self.assertEqual(self.finder.solve_finder([-2, -5, 0, -8, 3, 3], 3), -2)


if __name__ == "__main__":
    unittest.main()


