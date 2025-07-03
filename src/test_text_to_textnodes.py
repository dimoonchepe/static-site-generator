import unittest

from textnode import TextType, TextNode
from textnodes_tools import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_convert_text(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.PLAINTEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.PLAINTEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.PLAINTEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.PLAINTEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.PLAINTEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()


