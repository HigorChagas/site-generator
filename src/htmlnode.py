class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
        
    def to_html(self):
        raise NotImplementedError("Subclasses devem implementar to_html()")
    
    def props_to_html(self):
        if not self.props:
            return ""
        
        return "".join(f' {key}="{value}"' for key, value in self.props.items())
    
    def __repr__(self):
        return (
            f"HTMLNode(tag={self.tag!r}, value={self.value!r}, "
            f"children={self.children!r}, props={self.props!r})"
        )
        
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)
        
    def to_html(self):
        if self.value == None:
            raise ValueError("No value has been found")
        if self.tag == None:
            return self.value
        
        props_str = ""
        
        if self.props:
            props_str = " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())
        
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"