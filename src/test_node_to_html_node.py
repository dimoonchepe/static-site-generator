import unittest

from textnodes_tools import text_node_to_html_node
from textnode import TextNode, TextType
from leafnode import LeafNode


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_plain(self):
        node = TextNode("This is a text node", TextType.PLAINTEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), 'This is a text node')

    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<b>This is a bold text node</b>')

    def test_italic(self):
        node = TextNode("This is a italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<i>This is a italic text node</i>')

    def test_code(self):
        node = TextNode('print("hello world")', TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<code>print("hello world")</code>')

    def test_link(self):
        node = TextNode("Open me", TextType.LINK, "http://boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<a href="http://boot.dev">Open me</a>')

    def test_image(self):
        node = TextNode("Boots the bear", TextType.IMAGE, "http://boot.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<img src="http://boot.jpg" alt="Boots the bear"></img>')


if __name__ == "__main__":
    unittest.main()
