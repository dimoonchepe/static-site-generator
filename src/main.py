import os
from shutil import rmtree, copy
from markdown_to_html_node import markdown_to_html_node
from static_copy import recursive_copy_files
from textnodes_tools import extract_title

def main():
    recursive_copy_files('static', 'public')    
    generate_pages_recursive("content", "template.html", "public")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}") 
    file_content = ""
    template = ""
    with open(from_path, "r") as f:
        file_content = f.read()
    with open(template_path, "r") as f:
        template = f.read()
    html_node = markdown_to_html_node(file_content)
    html = html_node.to_html()
    title = extract_title(file_content)
    result = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    with open(dest_path, "w") as f:
        f.write(result)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    for path in os.listdir(dir_path_content):
        srcpath = os.path.join(dir_path_content, path)
        destpath = os.path.join(dest_dir_path, path)
        if os.path.isfile(srcpath):
            fileparts = path.split(".")
            if fileparts[-1] == 'md': 
                destpath = os.path.join(dest_dir_path, f"{".".join(fileparts[:-1])}.html")
                generate_page(srcpath, template_path, destpath)

        else:
            generate_pages_recursive(srcpath, template_path, destpath)

main()


