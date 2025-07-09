from bs4 import BeautifulSoup

input_file = input("Enter input HTML filename (e.g., blog.html): ").strip()

with open(input_file, "r", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

# Add {% load static %} at the beginning of <html>
load_static = soup.new_string('{% load static %}\n')
soup.html.insert(0, load_static)

# Convert <link> tags
for link in soup.find_all("link", href=True):
    href = link['href']
    if not href.startswith("http"):
        link['href'] = '{% static "' + href + '" %}'

# Convert <script> tags
for script in soup.find_all("script", src=True):
    src = script['src']
    if not src.startswith("http"):
        script['src'] = '{% static "' + src + '" %}'

# Convert <img> tags
for img in soup.find_all("img", src=True):
    src = img['src']
    if not src.startswith("http"):
        img['src'] = '{% static "' + src + '" %}'

output_file = "output.html"
with open(output_file, "w", encoding="utf-8") as file:
    file.write(str(soup))

print(f"Static conversion completed. Output saved to {output_file}")
