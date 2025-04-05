from markdown_to_html import convert_markdown_to_html

# Example markdown text with multiple elements
markdown = """# Markdown to HTML Converter

This is a **simple** demonstration of the markdown to HTML converter.

## Features

- Converts headings
- Supports **bold** and *italic* text
- Handles `inline code` and code blocks:

```python
def hello_world():
    print("Hello, World!")
```

Here's another code block without language specification:

```
# Some plain code
print("No language specified")
```

> This is a blockquote with a [link](https://example.com).

---

1. Ordered lists work too
2. Just like unordered lists
3. With proper numbering

![Example image](https://example.com/image.jpg)
"""

# Convert markdown to HTML
html = convert_markdown_to_html(markdown)

# Print the result
print("Original Markdown:")
print("-" * 80)
print(markdown)
print("-" * 80)
print("\nConverted HTML:")
print("-" * 80)
print(html)
print("-" * 80)

# Save the HTML to a file
output_file = 'converted_markdown.html'
with open(output_file, 'w') as f:
    # Add HTML document structure
    complete_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Converted Markdown</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }}
        code {{ background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px; }}
        pre {{ background-color: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto; }}
        blockquote {{ border-left: 4px solid #ccc; margin-left: 0; padding-left: 16px; color: #555; }}
        img {{ max-width: 100%; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; }}
        .language-python {{ color: #0058a8; }}
    </style>
</head>
<body>
{html}
</body>
</html>"""
    f.write(complete_html)

print(f"HTML content saved to '{output_file}'")