import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Test Link", {"href": "http://test.link", "color": "navy"})
        self.assertEqual(node.to_html(), '<a href="http://test.link" color="navy">Test Link</a>')

    def test_leaf_to_html_a(self):
        node = LeafNode("h1", "Header", { "color": "green"})
        self.assertEqual(node.to_html(), '<h1 color="green">Header</h1>')

if __name__ == "__main__":
    unittest.main()
