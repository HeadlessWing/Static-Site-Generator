from enum import Enum
from htmlnode import *
from textnode import *
import re
class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def markdown_to_blocks(markdown):
    final_blocks = []

    blocks = markdown.split("\n\n")
    for block in blocks:
        block = block.strip()
        if "\n" in block:
            block = block.replace("            ","")
        if block != "":
            final_blocks.append(block)

    return final_blocks

def block_to_block_type(block):
    lines = block.split("\n")
    if re.match(r'^#{1,6} .+', block):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    elif all(line.startswith("- ") for line in lines):
        return BlockType.ULIST
    
    check = True
    for i in range(0, len(lines)):
        if not lines[i].startswith(f"{i+1}. "):
            check = False
            break
    if check == True:
        return BlockType.OLIST
    else:
        return BlockType.PARAGRAPH
def text_to_children(text):
    children = []
    text_nodes = text_to_text_nodes(text)
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children

def mark_down_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_list = []
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                block_list.append(ParentNode("p", text_to_children(block)))
            case BlockType.HEADING:
                
            case BlockType.CODE:
                block_list.append(ParentNode("pre",[text_node_to_html_node(TextNode(block[3:-4],TextType.CODE))]))
            case BlockType.QUOTE:

            case BlockType.ULIST:

            case BlockType.OLIST:

