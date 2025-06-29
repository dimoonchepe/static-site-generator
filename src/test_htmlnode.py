import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {
            "fontSize":"16px",
            "color":"magenta"
        }
        node = HTMLNode("p", "this is a paragraph", None, props)
        expectedProps = 'fontSize="16px" color="magenta"'
        self.assertEqual(node.props_to_html(), expectedProps)

    def test_repr1(self):
        props = {
            "fontSize":"16px",
            "color":"magenta"
        }
        node = HTMLNode("p", "this is a paragraph", None, props)
        expectedRepr = '<p fontSize="16px" color="magenta">this is a paragraph</p>'
        self.assertEqual(f"{node}", expectedRepr)

    def test_children(self):
        nodeText = HTMLNode(value="this is a bold text")
        nodeb = HTMLNode("b", children=nodeText)
        expectedRepr = '<b>this is a bold text</b>'
        self.assertEqual(f"{nodeb}", expectedRepr)

if __name__ == "__main__":
    unittest.main()
