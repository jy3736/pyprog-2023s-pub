import re
import os
import sys

def transform_link(link):
    # Extract the file name from the link
    file_name = re.findall(r'/([^/]+\.(mp3))', link)[0]
    # Return the transformed link
    return '<audio src="./audio/week04/{}" controls></audio>'.format(file_name)

if len(sys.argv) < 2:
    print("Usage: python transform_links.py <html_file_path>")
    sys.exit()

html_file_path = sys.argv[1]
if not os.path.isfile(html_file_path):
    print("Invalid file path.")
    sys.exit()

with open(html_file_path, 'r',encoding="utf-8") as f:
    html = f.read()

# Find all links in the HTML code
#links = re.findall(r'href="(.*\.mp3)"', html)
pattern = re.compile(r'\<a[^>]*(.*?)\</a\>')
links = pattern.search(html)

# Transform each link and replace it in the HTML code
print(links.groups())

sys.exit()

# Write the transformed HTML code to a new file
new_html_file_path = os.path.splitext(html_file_path)[0] + '_transformed.html'
with open(new_html_file_path, 'w', encoding="utf-8") as f:
    f.write(html)

print("HTML file transformed and saved as {}.".format(new_html_file_path))
