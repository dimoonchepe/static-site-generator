import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_parent_to_html_leaf_children(self):
        children = [
            LeafNode(None, "This is a sentence with "),
            LeafNode("b", "Bold"),
            LeafNode(None, " text")            
        ]
        node = ParentNode("div", children)
        self.assertEqual(node.to_html(), "<div>This is a sentence with <b>Bold</b> text</div>")

    def test_parent_to_html_mixed_children(self):
        children = [
            LeafNode("div", "This is an unordered list:"),
            ParentNode("ul", [
                LeafNode("li", 'One'),
                LeafNode("li", 'Two'),
                LeafNode("li", 'Three'),
            ], props={"marker": "bullet"}),
            LeafNode(None, "---")            
        ]
        node = ParentNode("div", children)
        self.assertEqual(node.to_html(), '<div><div>This is an unordered list:</div><ul marker="bullet"><li>One</li><li>Two</li><li>Three</li></ul>---</div>')

if __name__ == "__main__":
    unittest.main()
