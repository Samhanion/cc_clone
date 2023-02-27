import re
from bs4 import BeautifulSoup

# Read in the HTML file
with open('futurelearn.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(content, 'html.parser')

# Find all img tags with both src and data-src attributes
for img in soup.find_all('img', src=True, **{'data-src': True}):
    # Replace the src attribute with the value of the data-src attribute
    img['src'] = img['data-src']

# Write the updated HTML to the file
with open('futurelearn.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
