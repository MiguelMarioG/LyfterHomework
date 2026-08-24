import unittest
from unittest.mock import patch, mock_open
from utility_function import read_lines

class TestReadLines(unittest.TestCase):

    @patch("utility_function.open", new_callable=mock_open, read_data="Line 1\nLine 2\nLine 3\n")
    def test_read_lines_success(self, mock_file):
        # arrange
        fake_path = "fake_file.txt"
        expected_lines = ["Line 1\n", "Line 2\n", "Line 3\n"]

        # act
        result = read_lines(fake_path)

        # assert
        self.assertEqual(result, expected_lines)
        mock_file.assert_called_once_with(fake_path, 'r')


    @patch("utility_function.open")
    def test_read_lines_file_not_found(self, mock_file):
        # arrange
        fake_path = "non_existent_file.txt"
        mock_file.side_effect = FileNotFoundError("The File not exist sorry")

        # act & assert
        with self.assertRaises(FileNotFoundError):
            read_lines(fake_path)

        mock_file.assert_called_once_with(fake_path, 'r')


if __name__ == "__main__":
    unittest.main()