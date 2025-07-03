import os
from markdown_to_html_node import markdown_to_html_node
from static_copy import recursive_copy_files
from textnodes_tools import extract_title

def main():
    recursive_copy_files('static', 'public')    
    generate_page("content/index.md", "template.html", "public/index.html")




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

main()


