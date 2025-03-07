class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

    def props_to_html(self):
        if self.props == None:
            return None
        result = ""
        for key in self.props:
            result += f'{key}="{self.props[key]} '
        return result
    
    def __repr__(self):
        return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"
        