import re
from textblocks import BlockType, block_to_block_type, markdown_to_blocks
from main import text_to_textnodes, text_node_to_html_node
from parentnode import ParentNode
from leafnode import LeafNode

def markdown_to_html_node(md):
    blocks = markdown_to_blocks(md)
    nodes = []

    for block in blocks:
        match block_to_block_type(block):
            case BlockType.PARAGRAPH:
                nodes.append(ParentNode("p", block_to_html_nodes(block.replace('\n',' '))))
            case BlockType.QUOTE:                 
                nodes.append(ParentNode("blockquote", block_to_html_nodes(strip_quote_marks(block))))
            case BlockType.ULIST:
                nodes.append(create_ulist(block))
            case BlockType.OLIST:
                nodes.append(create_olist(block))
            case BlockType.CODE:
                nodes.append(ParentNode("pre", [ParentNode("code", [LeafNode(None, block[3:-3].lstrip())])]))
            case BlockType.HEADING:
                nodes.append(create_heading(block))
            case _:
                raise Exception("Unknown block type")
    return ParentNode("div", nodes)


def block_to_html_nodes(text):
    text_nodes = text_to_textnodes(text)  
    nodes = []
    for text_node in text_nodes:
        nodes.append(text_node_to_html_node(text_node))
    return nodes


def strip_quote_marks(text):
    lines = text.split('/n')
    result = []
    for line in lines:
        result.append(re.sub(r"^>", "", line))


def create_ulist(block):
    lines = block.split('/n')
    items = []
    for line in lines:
        items.append(LeafNode("li", re.sub("^- ", "", line)))
    return ParentNode("ul", items)


def create_olist(block):
    lines = block.split('/n')
    items = []
    for line in lines:
        items.append(LeafNode("li", re.sub("^\d+. ", "", line)))
    return ParentNode("ol", items)


def create_heading(text):
    level = 0
    while text[level] == '#':
        level += 1
    return ParentNode(f"h{level}", text[level+1:])