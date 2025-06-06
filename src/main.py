import os
import shutil
import sys
from gencontent import generate_pages_recursive

def main():
    public_path = "./docs"
    static_path = "./static"
    content_path = "./content"
    template_path = "./template.html"
    
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = '/'

    # remove and recreate the dest dir if it exits, otherwise just create it
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
        os.mkdir(public_path)
    else:
        os.mkdir(public_path)
    copy_contents(static_path, public_path)

    generate_pages_recursive(content_path, template_path, public_path, basepath)

def copy_contents(src, dest):
    src_contents = os.listdir(src)
    for item in src_contents:
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)
        if os.path.isfile(src_path):
            #copy the file to the same location in the dest path
            shutil.copy(src_path, dest_path)
        else:
            # create the directory at the current path in the dest directory and pass both of these into the recursive function
            os.mkdir(dest_path)
            copy_contents(src_path, dest_path)
    return

if __name__ == "__main__":
    main()