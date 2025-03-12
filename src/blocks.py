from enum import Enum
from htmlnode import *
from textnode import *

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

