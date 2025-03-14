import re

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_title(markdown):
    lines = markdown.split("\n\n")
    for line in lines:
        if line.startswith("# ") == True:
            return line.strip()[2:].strip()