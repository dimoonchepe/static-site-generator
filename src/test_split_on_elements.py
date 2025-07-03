import unittest

from textnode import TextType, TextNode
from textnodes_tools import split_nodes_image, split_nodes_link


class TestSplitOnElements(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png), and the first image again ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.PLAINTEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAINTEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAINTEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                TextNode(", and the first image again ", TextType.PLAINTEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
                "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png), and the first link again [link](https://i.imgur.com/zjjcJKZ.png)",
            TextType.PLAINTEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.PLAINTEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAINTEXT),
                TextNode("second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"),
                TextNode(", and the first link again ", TextType.PLAINTEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()


