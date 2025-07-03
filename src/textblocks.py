import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "ulist"
    OLIST = "olist"


def markdown_to_blocks(text):
    return list(filter(lambda t: len(t) > 0, map(lambda s: s.strip(), text.split('\n\n'))));


def block_to_block_type(block):
    if re.match(r"#{1,5} ", block):
        return BlockType.HEADING
    if block.startswith('```') and block.endswith('```'):
        return BlockType.CODE
    lines = block.split('\n')
    if all(map(lambda line: line.startswith('>'), lines)):
        return BlockType.QUOTE
    if all(map(lambda line: line.startswith('- '), lines)):
        return BlockType.ULIST
    for i in range(len(lines)):
        if not lines[i].startswith(f"{i + 1}. "):
            return BlockType.PARAGRAPH
    return BlockType.OLIST
    


