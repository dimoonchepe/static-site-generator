from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode should have a value")
        if not self.tag:
            return self.value
        props = self.props_to_html()
        props_text = f"{' ' if props else ''}{props}"
        return f"<{self.tag}{props_text}>{self.value}</{self.tag}>"
        
