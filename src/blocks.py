from enum import Enum
from htmlnode import *
from textnode import *

def markdown_to_blocks(markdown):
    final_blocks = []

    blocks = markdown.strip('""').split("\n\n")
    for block in blocks:
        block = block.strip()
        if block != "":
            final_blocks.append(block)

    return final_blocks

