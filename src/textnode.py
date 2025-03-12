from enum import Enum
from htmlnode import *
from extract import *
class TextType(Enum):
    TEXT = "Normal Text"
    BOLD = "Bold Text"
    ITALIC = "Italic"
    CODE = "Code Text"
    LINK = "Link"
    IMAGE = "Image"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    
    match text_node.text_type:
        
        case TextType.TEXT:
            return LeafNode( None, text_node.text)
        case TextType.BOLD:
            return LeafNode( "b", text_node.text)
        case TextType.ITALIC:
            return LeafNode( "i", text_node.text)
        case TextType.CODE:
            return LeafNode( "code", text_node.text)
        case TextType.LINK:
            return LeafNode( "a", text_node.text, {"href": f"{text_node.url}"})
        case TextType.IMAGE:
            return LeafNode( "img", "", {"src": f"{text_node.url}", "alt": f"{text_node.text}" })
        case _:
            raise ValueError(f"invalid text type: {text_node.text_type}")
        
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        node_split = node.text.split(delimiter)
        split_list = []
        if len(node_split) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range (0, len(node_split)):
            if node_split[i] == "":
                continue
            if i % 2 == 0:
                split_list.append(TextNode(node_split[i], TextType.TEXT))
            else:
                split_list.append(TextNode(node_split[i], text_type))
        new_nodes.extend(split_list)
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        node_list = []
        tuple_list = extract_markdown_images(node.text)
        if len(tuple_list) == 0:
            new_nodes.append(node)
            continue
        for tuple in tuple_list:
            node.text = node.text.split(f"![{tuple[0]}]({tuple[1]})", 1)
            if len(node.text) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if node.text[0] != "":
                node_list.append(TextNode(node.text[0], TextType.TEXT))
            node_list.append(TextNode(tuple[0], TextType.IMAGE, tuple[1]))
            node.text = str(node.text[1])
        if node.text != "":
            node_list.append(TextNode(node.text, TextType.TEXT))
        new_nodes.extend(node_list)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        node_list = []
        tuple_list = extract_markdown_links(node.text)
        if len(tuple_list) == 0:
            new_nodes.append(node)
            continue
        for tuple in tuple_list:
            node.text = node.text.split(f"[{tuple[0]}]({tuple[1]})", 1)
            if len(node.text) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if node.text[0] != "":
                node_list.append(TextNode(node.text[0], TextType.TEXT))
            node_list.append(TextNode(tuple[0], TextType.LINK, tuple[1]))
            node.text = str(node.text[1])
        if node.text != "":
            node_list.append(TextNode(node.text, TextType.TEXT))
        new_nodes.extend(node_list)
    return new_nodes

def text_to_text_nodes(text):
    return split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(split_nodes_image(split_nodes_link(text)),"**", TextType.BOLD),"`", TextType.CODE), "_", TextType.ITALIC)