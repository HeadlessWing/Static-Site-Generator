from enum import Enum
from htmlnode import *
from textnode import *
import re
import textwrap

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def markdown_to_blocks(markdown):
    markdown = textwrap.dedent(markdown)
    final_blocks = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        block = block.strip()
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

def count_header(block):
    for i in range (1,5):
        if block[i] != "#":
            return i
    return 6


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_list = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                lines = block.split("\n")
                paragraph = " ".join(lines)
                block_list.append(ParentNode("p", text_to_children([TextNode(paragraph, TextType.TEXT)])))
            case BlockType.HEADING:
                i = count_header(block)
                block_list.append(ParentNode(f"h{i}", text_to_children([TextNode(block[i+1:], TextType.TEXT)])))
            case BlockType.CODE:
                block_list.append(ParentNode("pre",[text_node_to_html_node(TextNode(block[4:-3],TextType.CODE))]))
            case BlockType.QUOTE:
                lines = block.split("\n")
                new_lines = []
                for line in lines:
                    new_lines.append(line.lstrip("> "))
                paragraph = " ".join(new_lines)
                block_list.append(ParentNode("blockquote", text_to_children([TextNode(paragraph, TextType.TEXT)])))
            case BlockType.ULIST:
                children = []
                list_lines = block.split("\n")
                for line in list_lines:
                    children.append(ParentNode("li",text_to_children([TextNode(line[2:], TextType.TEXT)])))
                block_list.append(ParentNode("ul", children))
            case BlockType.OLIST:
                children = []
                list_lines = block.split("\n")
                for line in list_lines:
                    children.append(ParentNode("li",text_to_children([TextNode(line[3:], TextType.TEXT)])))
                block_list.append(ParentNode("ol", children))
    return ParentNode("div", block_list)

