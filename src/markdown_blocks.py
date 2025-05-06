from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def markdown_to_blocks(markdown):
    string_list = markdown.split("\n\n")
    return [string.strip() for string in string_list if string.strip() != ""]

def block_to_block_type(block):
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    lines = block.split("\n")
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    if all(line.startswith("* ") or line.startswith("- ") for line in lines):
        return BlockType.ULIST
    if all(line.startswith(f"{i+1}. ") for i, line in enumerate(lines)):
        return BlockType.OLIST
    else:
        return BlockType.PARAGRAPH
    
def markdown_to_html_node(markdown):
    pass