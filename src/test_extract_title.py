
import unittest

from textnodes_tools import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        markdown = '# Hello'
        title = extract_title(markdown)
        self.assertEqual(title, 'Hello')

    def test_next_line(self):
        markdown = """
this is some generic text

## This is not a title

# Excalibur!    

some other text
"""
        
        title = extract_title(markdown)
        self.assertEqual(title, 'Excalibur!')


if __name__ == "__main__":
    unittest.main()
