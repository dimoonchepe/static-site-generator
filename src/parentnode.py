from htmlnode import HTMLNode
from functools import reduce

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.children:
            raise ValueError("ParentNode should have children")
        if not self.tag:
            raise ValueError("ParentNode should have a tag")
        props = self.props_to_html()
        props_text = f"{' ' if props else ''}{props}"
        innerHtml = reduce(lambda html, node: html + node.to_html(), self.children, "")
        return f"<{self.tag}{props_text}>{innerHtml}</{self.tag}>"
        
