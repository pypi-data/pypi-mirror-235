# Contentful Rich Text To Markdown Converter

This module converts Contentful Rich Text objects to Markdown. It is a python wrapper for a node module [contentful-rich-text-to-markdown](https://www.npmjs.com/package/contentful-rich-text-to-markdown-converter)

## Installation

```bash
pip install contentful-rich-text-to-markdown-converter
```

## Usage

```python
import contentful
from contentful_rich_text_to_markdown_converter import convert_rich_text_to_markdown

# Connect to Contentful API
client = contentful.Client('<your_contentful_space_id>',' <your_contentful_access_token>')

# Get a rich text field from from your contentful space
rich_text = client.entry('<your_entry_id>').rich_text_field

# Convert rich text to markdown
markdown = convert_rich_text_to_markdown(test_rich_text)

```
