import os
from markdown_blocks import markdown_to_blocks, markdown_to_html_node

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if len(block) >= 3 and block[0:2] == "# ":
            return block[2:]
    raise Exception("No h1 header found")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Genrating page from {from_path} to {dest_path} using {template_path}")
    # Read the markdown file from from_path and store the contents in a variable
    from_path_contents = ""
    template_path_contents = ""
    with open(from_path, "r", encoding="utf-8") as file_object:
        from_path_contents = file_object.read()
    # Read the template file at template_path and store the contents in a variable
    with open(template_path, "r", encoding="utf-8") as file_object:
        template_path_contents = file_object.read()
    # Convert the markdown file to an html string
    markdown_html = markdown_to_html_node(from_path_contents).to_html()
    title = extract_title(from_path_contents)
    template_path_contents = template_path_contents.replace("{{ Title }}", title).replace("{{ Content }}", markdown_html).replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')

    # Write the new full HTML page to a file at dest_path
    dir_path = os.path.dirname(dest_path)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path)
    
    with open(dest_path, "w") as file_object:
        file_object.write(template_path_contents)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    content_path_contents = os.listdir(dir_path_content)
    for item in content_path_contents:
        src_item_path = os.path.join(dir_path_content, item)
        dest_item_path = os.path.join(dest_dir_path, item)

        if os.path.isfile(src_item_path):
            # Check if the file is a markdown file
            if item.endswith(".md"):
                # For markdown files, change extension to .html for destination
                html_filename = item[:-3] + ".html"
                dest_file_path = os.path.join(dest_dir_path, html_filename)
                generate_page(src_item_path, template_path, dest_file_path, basepath)
        elif os.path.isdir(src_item_path):
            # If it's a directory, create the corresponding directory in the destination
            # and then recurse.
            # dest_item_path is the new destination directory for the recursion
            if not os.path.exists(dest_item_path):
                os.makedirs(dest_item_path)
            generate_pages_recursive(src_item_path, template_path, dest_item_path, basepath)