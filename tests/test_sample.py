import unittest
import sys
import pytest as pt
from fluentcheck import Check


class TestSample(unittest.TestCase):

    def test_pytest_is_working(self):
        self.assertIsNotNone(Check)
        self.assertIsNotNone(pt)

    def test_python_version(self):
        self.assertEqual(sys.version_info.major, 3)
        self.assertGreaterEqual(sys.version_info.minor, 10)


if __name__ == "__main__":
    unittest.main()
