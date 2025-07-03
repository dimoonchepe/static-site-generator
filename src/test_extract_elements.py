import unittest

from textnodes_tools import extract_markdown_images, extract_markdown_links


class TestExtractEntities(unittest.TestCase):
    def test_extract_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


    def test_extract_links(self):
        matches = extract_markdown_links(
            "This is text with an [BootDev](https://boot.dev)"
        )
        self.assertListEqual([("BootDev", "https://boot.dev")], matches)


if __name__ == "__main__":
    unittest.main()

