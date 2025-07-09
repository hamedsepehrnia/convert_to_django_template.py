````markdown
# Convert to Django Template

A Python script to automatically convert local asset links (CSS, JS, images) in an HTML file to Django `{% static %}` template tags and add `{% load static %}` at the beginning.

## Features

- Parses an input HTML file.
- Converts local `href` and `src` attributes in `<link>`, `<script>`, and `<img>` tags to Django static tags.
- Adds `{% load static %}` at the start of the HTML for Django template usage.
- Saves the output to `output.html`.

## Requirements

- Python 3.x
- BeautifulSoup4 library (`bs4`)

## Installation

```bash
pip install beautifulsoup4
````

## Usage

Run the script and enter the input HTML filename when prompted:

```bash
python convertor.py
```

Example:

```
Enter input HTML filename (e.g., blog.html): blog.html
Static conversion completed. Output saved to output.html
```


