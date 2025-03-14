from textnode import *
from htmlnode import *
import os
import shutil
from extract import extract_title
from blocks import markdown_to_html_node
dir_path_static = "./static"
dir_path_public = "./public"

def copy_static_to_public():
    if os.path.exists(dir_path_static) == False: # or 
        raise Exception("required paths do not exist")
    if os.path.exists(dir_path_public) == True:
        shutil.rmtree(dir_path_public)
    os.mkdir(dir_path_public)
    copy_dir(dir_path_static, dir_path_public )

def copy_dir(origin, destination):
    files = os.listdir(origin)
    for file in files:

        n_origin = os.path.join(origin, file)
        if os.path.isfile(n_origin) == True:
            shutil.copy(n_origin, destination)
        if os.path.isdir(n_origin) == True:
            n_destination = os.path.join(destination, file)
            os.mkdir(n_destination)
            copy_dir(n_origin, n_destination)

def generate_page(from_path, dest_path, template_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as file:
        markdown = file.read()
    with open(template_path) as file:
        template = file.read()
    title = extract_title(markdown)
    content = markdown_to_html_node(markdown)
    new_page = template.replace("{{ Title }}", title).replace("{{ Content }}", content.to_html())
    
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(f"{dest_path}/index.html", "w") as file:
        file.write(new_page)
def generate_pages_recursive(dir_path_contents, template_path, dest_dir_path):
    files = os.listdir(dir_path_contents)
    for file in files:
        n_origin = os.path.join(dir_path_contents, file)
        if os.path.isfile(n_origin) == True:
            generate_page(n_origin, dest_dir_path, template_path)
        if os.path.isdir(n_origin) == True:
            n_destination = os.path.join(dest_dir_path, file)
            os.mkdir(n_destination)
            generate_pages_recursive(n_origin, template_path, n_destination)

def main():
    copy_static_to_public()
    generate_pages_recursive("./content", "./template.html", "public/")


main()