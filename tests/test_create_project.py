import unittest
from unittest.mock import MagicMock
import vite

class ViteTest(unittest.TestCase):
    def test_create_project(self):
        mock_path = MagicMock('xD')
        vite.create_project(mock_path)
        mock_path.assert_called_with('xD')

if __name__ == '__main__':
    unittest.main()
