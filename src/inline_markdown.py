import re
from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    split_nodes_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            split_nodes_list.append(node)
        else:
            split_text = node.text.split(delimiter)
            if len(split_text) % 2 == 0:
                raise ValueError("Invalid syntax: No closing delimiter found")
            for i in range(len(split_text)):
                if i % 2 == 0 and split_text[i]:
                    split_nodes_list.append(TextNode(split_text[i], TextType.TEXT))
                elif i % 2 == 1 and split_text[i]:
                    split_nodes_list.append(TextNode(split_text[i], text_type))
    return split_nodes_list

def split_nodes_image(old_nodes):
    split_nodes_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT or not extract_markdown_images(node.text):
            split_nodes_list.append(node)
        else:
            remaining_text = node.text
            while True:
                images_in_remaining = extract_markdown_images(remaining_text)
                if not images_in_remaining:
                    if remaining_text:
                        split_nodes_list.append(TextNode(remaining_text, TextType.TEXT))
                    break # Exit while loop once no more images are found
                
                alt_text, url = images_in_remaining[0]
                delimiter_string = f"![{alt_text}]({url})"
                split_string_list = remaining_text.split(delimiter_string, 1)

                if len(split_string_list) != 2:
                    raise ValueError(f"Invalid markdown, image not found where expected: {delimiter_string} in {remaining_text}")
                before_text = split_string_list[0]
                if before_text:
                    split_nodes_list.append(TextNode(before_text, TextType.TEXT))
                split_nodes_list.append(TextNode(alt_text, TextType.IMAGE, url))
                remaining_text = split_string_list[1]
    return split_nodes_list

def split_nodes_link(old_nodes):
    split_nodes_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT or not extract_markdown_links(node.text):
            split_nodes_list.append(node)
        else:
            remaining_text = node.text
            while True:
                links_in_remaining = extract_markdown_links(remaining_text)
                if not links_in_remaining:
                    if remaining_text:
                        split_nodes_list.append(TextNode(remaining_text, TextType.TEXT))
                    break # Exit while loop once no more links are found
                
                link_text, url = links_in_remaining[0]
                delimiter_string = f"[{link_text}]({url})"
                split_string_list = remaining_text.split(delimiter_string, 1)

                if len(split_string_list) != 2:
                    raise ValueError(f"Invalid markdown, image not found where expected: {delimiter_string} in {remaining_text}")
                before_text = split_string_list[0]
                if before_text:
                    split_nodes_list.append(TextNode(before_text, TextType.TEXT))
                split_nodes_list.append(TextNode(link_text, TextType.LINK, url))
                remaining_text = split_string_list[1]
    return split_nodes_list

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def text_to_textnodes(text):
    pass