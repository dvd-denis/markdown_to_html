# Markdown to HTML Converter

A simple Python library that converts Markdown text to HTML.

## Installation

```bash
# Install with uv
uv pip install .
```

## Usage

```python
from md_converter import convert_markdown_to_html

markdown = "# Hello World\n\nThis is **bold** and *italic* text."
html = convert_markdown_to_html(markdown)
print(html)
# Output:
# <h1>Hello World</h1>
# <p>This is <strong>bold</strong> and <em>italic</em> text.</p>
```

## Features

- Headings (h1-h6)
- Paragraphs
- Bold and italic text
- Code blocks and inline code
- Lists (ordered and unordered)
- Links and images
- Blockquotes
- Horizontal rules 
