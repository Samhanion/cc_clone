import os
from bs4 import BeautifulSoup
from googletrans import Translator
import subprocess
import re



# Function to apply to each HTML file
def process_html_file(filepath):
    # Read in the HTML file
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Create a BeautifulSoup object
    soup = BeautifulSoup(content, 'html.parser')

    # Find all img tags with both src and data-src attributes
    for img in soup.find_all('img', src=True, **{'data-src': True}):
        # Replace the src attribute with the value of the data-src attribute
        img['src'] = img['data-src']

    # Write the updated HTML to the file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))



        


count = 275
# Function to traverse folder and apply code to HTML files
def traverse_folder(folder_path):
    global count
    # Iterate over all files and directories in the folder
    for item in os.listdir(folder_path):
        # Get the full path of the item
        item_path = os.path.join(folder_path, item)
        
        # If the item is a directory, recursively traverse it
        if os.path.isdir(item_path):
            traverse_folder(item_path)
        # If the item is an HTML file, apply the code to it
        
        elif os.path.isfile(item_path) and item_path.endswith('.html'):
            print(item_path)
            process_html_file(item_path)
            count -= 1
            print(str(count) + ' FILES REMAINING')



# Main function
if __name__ == '__main__':
    folder_path = './www.classcentral.com' # Replace with the path to the folder you want to traverse
    traverse_folder(folder_path)
    
