from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    string_list = markdown.split("\n\n")
    return [string.strip() for string in string_list if string.strip() != ""]

def block_to_block_type(block_text):
    pass