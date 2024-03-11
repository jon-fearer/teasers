import unittest

from . import rotate


class TestRotate(unittest.TestCase):
    def test_rotate_twice(self) -> None:
        self.assertEqual(rotate.rotate([1, 2, 3, 4, 5, 6], 2), [5, 6, 1, 2, 3, 4])

    def test_rotate_thrice(self) -> None:
        self.assertEqual(rotate.rotate([1, 2, 3, 4, 5, 6], 3), [4, 5, 6, 1, 2, 3])

