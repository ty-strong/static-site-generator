# Static Site Generator

A simple static site generator written in Python. Converts your Markdown content into a static website using a customizable HTML template.

## Features

- Converts Markdown files in the `content/` directory to HTML pages
- Uses a customizable `template.html` as the layout
- Simple build process with a shell script

## Requirements

- Python 3.x

## Getting Started

1. Place your Markdown (`.md`) files in the `content/` directory.
2. Edit the `template.html` file in the root directory to customize your site layout.
3. Build the site:
    ```bash
    ./build.sh
    ```
   The generated HTML files will be output to the appropriate directory.

## License

MIT License

---

*Made with Python for simple static site generation.*
