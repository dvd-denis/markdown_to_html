import unittest
from markdown_to_html.converter import convert_markdown_to_html

class TestMarkdownConverter(unittest.TestCase):
    def test_paragraph(self):
        markdown = "This is a paragraph."
        expected = "<p>This is a paragraph.</p>"
        self.assertEqual(convert_markdown_to_html(markdown), expected)
    
    def test_multiple_paragraphs(self):
        markdown = "This is paragraph 1.\n\nThis is paragraph 2."
        expected = "<p>This is paragraph 1.</p>\n<p>This is paragraph 2.</p>"
        self.assertEqual(convert_markdown_to_html(markdown), expected)
    
    def test_headings(self):
        markdown = "# Heading 1\n\n## Heading 2\n\n### Heading 3"
        expected = "<h1>Heading 1</h1>\n<h2>Heading 2</h2>\n<h3>Heading 3</h3>"
        self.assertEqual(convert_markdown_to_html(markdown), expected)
    
    def test_bold(self):
        markdown = "This is **bold** text."
        expected = "<p>This is <strong>bold</strong> text.</p>"
        self.assertEqual(convert_markdown_to_html(markdown), expected)
    
    def test_italic(self):
        markdown = "This is *italic* text."
        expected = "<p>This is <em>italic</em> text.</p>"
        self.assertEqual(convert_markdown_to_html(markdown), expected)
    
    def test_inline_code(self):
        markdown = "This is `inline code`."
        expected = "<p>This is <code>inline code</code>.</p>"
        self.assertEqual(convert_markdown_to_html(markdown), expected)
    
    def test_code_block(self):
        markdown = "```\ncode block\nmultiple lines\n```"
        expected = "<pre><code>code block\nmultiple lines</code></pre>"
        self.assertEqual(convert_markdown_to_html(markdown), expected)
    
    def test_code_block_with_language(self):
        markdown = "```python\ndef hello_world():\n    print('Hello, World!')\n```"
        expected = '<pre><code class="language-python">def hello_world():\n    print(\'Hello, World!\')</code></pre>'
        self.assertEqual(convert_markdown_to_html(markdown), expected)
    
    def test_unordered_list(self):
        markdown = "- Item 1\n- Item 2\n- Item 3"
        expected = "<ul>\n<li>Item 1</li>\n<li>Item 2</li>\n<li>Item 3</li>\n</ul>"
        self.assertEqual(convert_markdown_to_html(markdown), expected)
    
    def test_ordered_list(self):
        markdown = "1. Item 1\n2. Item 2\n3. Item 3"
        expected = "<ol>\n<li>Item 1</li>\n<li>Item 2</li>\n<li>Item 3</li>\n</ol>"
        self.assertEqual(convert_markdown_to_html(markdown), expected)
    
    def test_links(self):
        markdown = "This is a [link](https://example.com)."
        expected = "<p>This is a <a href=\"https://example.com\">link</a>.</p>"
        self.assertEqual(convert_markdown_to_html(markdown), expected)
    
    def test_images(self):
        markdown = "![alt text](image.jpg)"
        expected = "<p><img src=\"image.jpg\" alt=\"alt text\"></p>"
        self.assertEqual(convert_markdown_to_html(markdown), expected)
    
    def test_blockquote(self):
        markdown = "> This is a blockquote."
        expected = "<blockquote>\n<p>This is a blockquote.</p>\n</blockquote>"
        self.assertEqual(convert_markdown_to_html(markdown), expected)
    
    def test_horizontal_rule(self):
        markdown = "---"
        expected = "<hr>"
        self.assertEqual(convert_markdown_to_html(markdown), expected)
    
    def test_combined_elements(self):
        markdown = "# Heading\n\nParagraph with **bold** and *italic* text.\n\n- List item 1\n- List item 2"
        expected = "<h1>Heading</h1>\n<p>Paragraph with <strong>bold</strong> and <em>italic</em> text.</p>\n<ul>\n<li>List item 1</li>\n<li>List item 2</li>\n</ul>"
        self.assertEqual(convert_markdown_to_html(markdown), expected)

if __name__ == "__main__":
    unittest.main() 