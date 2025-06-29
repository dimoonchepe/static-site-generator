class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if not bool(self.props):
            return ""
        res = []
        for key in self.props:
            res.append(f'{key}="{self.props[key]}"')
        return " ".join(res)

    def __repr__(self):
        props = self.props_to_html()
        return f'{"<" if self.tag else ""}{self.tag or ""}{" " if props else ""}{props}{">" if self.tag else ""}{self.value or ""}{self.children or ""}{"</" if self.tag else ""}{self.tag or ""}{">" if self.tag else ""}'


