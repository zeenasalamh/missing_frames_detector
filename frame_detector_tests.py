import unittest
from video_frame_detector import find_missing_ranges


class TestMissingFrames(unittest.TestCase):
    
    def test_example_case(self):
        frames = [1, 2, 3, 5, 6, 10, 11, 16]
        expected = {
            "gaps": [[4, 4], [7, 9], [12, 15]],
            "longest_gap": [12, 15],
            "missing_count": 8
        }
        result = find_missing_ranges(frames)
        self.assertEqual(result, expected)
    
    def test_no_missing_frames(self):
        frames = [1, 2, 3, 4, 5]
        expected = {
            "gaps": [],
            "longest_gap": None,
            "missing_count": 0
        }
        result = find_missing_ranges(frames)
        self.assertEqual(result, expected)
    
    def test_single_frame(self):
        frames = [1]
        expected = {
            "gaps": [],
            "longest_gap": None,
            "missing_count": 0
        }
        result = find_missing_ranges(frames)
        self.assertEqual(result, expected)
    
    def test_large_gap(self):
        frames = [1, 10]
        expected = {
            "gaps": [[2, 9]],
            "longest_gap": [2, 9],
            "missing_count": 8
        }
        result = find_missing_ranges(frames)
        self.assertEqual(result, expected)
    
    def test_multiple_small_gaps(self):
        frames = [1, 3, 5, 7, 9]
        expected = {
            "gaps": [[2, 2], [4, 4], [6, 6], [8, 8]],
            "longest_gap": [2, 2],
            "missing_count": 4
        }
        result = find_missing_ranges(frames)
        self.assertEqual(result, expected)
    
    def test_starting_from_non_one(self):
        frames = [5, 6, 7, 8, 9]
        expected = {
            "gaps": [[1, 4]],
            "longest_gap": [1, 4],
            "missing_count": 4
        }
        result = find_missing_ranges(frames)
        self.assertEqual(result, expected)
    
    def test_empty_list(self):
        frames = []
        expected = {
            "gaps": [],
            "longest_gap": None,
            "missing_count": 0
        }
        result = find_missing_ranges(frames)
        self.assertEqual(result, expected)
    
    def test_unordered_input(self):
        frames = [16, 3, 1, 11, 6, 2, 5, 10]
        expected = {
            "gaps": [[4, 4], [7, 9], [12, 15]],
            "longest_gap": [12, 15],
            "missing_count": 8
        }
        result = find_missing_ranges(frames)
        self.assertEqual(result, expected)
    
    def test_missing_at_end(self):
        frames = [1, 2, 3, 4, 5, 7, 8]
        expected = {
            "gaps": [[6, 6]],
            "longest_gap": [6, 6],
            "missing_count": 1
        }
        result = find_missing_ranges(frames)
        self.assertEqual(result, expected)
    
    def test_missing_at_beginning(self):
        frames = [3, 4, 5, 6, 7]
        expected = {
            "gaps": [[1, 2]],
            "longest_gap": [1, 2],
            "missing_count": 2
        }
        result = find_missing_ranges(frames)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
