import re

def convert_markdown_to_html(markdown):
    """
    Convert a markdown string to HTML.
    
    Args:
        markdown (str): The markdown text to convert
    
    Returns:
        str: The HTML representation of the markdown
    """
    # Split the markdown into paragraphs first (this preserves paragraph structure)
    paragraphs = markdown.split('\n\n')
    processed_paragraphs = []
    
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        
        # Process code blocks first (```)
        # Check for language-specific code blocks like ```python
        code_block_pattern = re.compile(r'```(\w*)\n(.*?)```', re.DOTALL)
        if code_block_pattern.search(para):
            processed = code_block_pattern.sub(
                lambda m: process_code_block(m.group(1), m.group(2)),
                para
            )
            processed_paragraphs.append(processed)
            continue
        
        # Process horizontal rules
        if re.match(r'^---+$', para):
            processed_paragraphs.append('<hr>')
            continue
        
        # Process headings
        if para.startswith('# '):
            processed = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', para)
            processed_paragraphs.append(processed)
            continue
        elif para.startswith('## '):
            processed = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', para)
            processed_paragraphs.append(processed)
            continue
        elif para.startswith('### '):
            processed = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', para)
            processed_paragraphs.append(processed)
            continue
        elif para.startswith('#### '):
            processed = re.sub(r'^#### (.*?)$', r'<h4>\1</h4>', para)
            processed_paragraphs.append(processed)
            continue
        elif para.startswith('##### '):
            processed = re.sub(r'^##### (.*?)$', r'<h5>\1</h5>', para)
            processed_paragraphs.append(processed)
            continue
        elif para.startswith('###### '):
            processed = re.sub(r'^###### (.*?)$', r'<h6>\1</h6>', para)
            processed_paragraphs.append(processed)
            continue
        
        # Process blockquotes
        if para.startswith('> '):
            lines = para.split('\n')
            quote_content = []
            for line in lines:
                if line.startswith('> '):
                    # Extract content without the blockquote marker
                    content = line[2:]
                    # Process inline elements
                    content = process_inline_elements(content)
                    quote_content.append(content)
            
            quote_html = "<blockquote>\n<p>" + "</p>\n<p>".join(quote_content) + "</p>\n</blockquote>"
            processed_paragraphs.append(quote_html)
            continue
        
        # Process unordered lists
        if re.match(r'^- ', para.split('\n')[0]):
            lines = para.split('\n')
            list_items = []
            for line in lines:
                if line.startswith('- '):
                    # Process inline elements in list items
                    content = process_inline_elements(line[2:])
                    list_items.append(f"<li>{content}</li>")
            
            list_html = "<ul>\n" + "\n".join(list_items) + "\n</ul>"
            processed_paragraphs.append(list_html)
            continue
        
        # Process ordered lists
        if re.match(r'^\d+\. ', para.split('\n')[0]):
            lines = para.split('\n')
            list_items = []
            for line in lines:
                item_match = re.match(r'^\d+\. (.*?)$', line)
                if item_match:
                    # Process inline elements in list items
                    content = process_inline_elements(item_match.group(1))
                    list_items.append(f"<li>{content}</li>")
            
            list_html = "<ol>\n" + "\n".join(list_items) + "\n</ol>"
            processed_paragraphs.append(list_html)
            continue
        
        # Process inline elements for regular paragraphs
        processed = process_inline_elements(para)
        
        # Add paragraph tags
        processed_paragraphs.append(f"<p>{processed}</p>")
    
    html = '\n'.join(processed_paragraphs)
    
    return html

def process_code_block(language, code):
    """Process code blocks with optional language specification."""
    code = code.strip()
    if language:
        return f'<pre><code class="language-{language}">{code}</code></pre>'
    else:
        return f'<pre><code>{code}</code></pre>'

def process_inline_elements(text):
    """Process inline markdown elements within a text string."""
    # Bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    
    # Italic
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    
    # Inline code
    text = re.sub(r'`(.*?)`', r'<code>\1</code>', text)
    
    # Images - needs to be processed before links
    text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', text)
    
    # Links
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)
    
    return text 