from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: tag field is required")
        elif self.children is None:
            raise ValueError("invalid HTML: children field is required")
        else:
            html_string=""
            for child in self.children:
                html_string += child.to_html()
            return f"<{self.tag}{self.props_to_html()}>{html_string}</{self.tag}>"
        
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"