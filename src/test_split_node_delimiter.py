import unittest

from textnodes_tools import split_nodes_delimiter
from textnode import TextNode, TextType
from leafnode import LeafNode


class TestSplitNodeDelimiter(unittest.TestCase):
    def test_bold(self):
        nodes = [TextNode("This is a **bold** text", TextType.PLAINTEXT)]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(f"{new_nodes[0]}", 'TextNode("This is a ", text, None)')
        self.assertEqual(f"{new_nodes[1]}", 'TextNode("bold", bold, None)')
        self.assertEqual(f"{new_nodes[2]}", 'TextNode(" text", text, None)')

    def test_code(self):
        nodes = [TextNode("This is a text with `some code`", TextType.PLAINTEXT)]
        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 2)
        self.assertEqual(f"{new_nodes[0]}", 'TextNode("This is a text with ", text, None)')
        self.assertEqual(f"{new_nodes[1]}", 'TextNode("some code", code, None)')


if __name__ == "__main__":
    unittest.main()
