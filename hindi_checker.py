import os
from bs4 import BeautifulSoup
import codecs

# Define a function to check if a string contains any Hindi characters
def is_hindi(title):
    # Create a set of Unicode code points for Hindi characters
    hindi_chars = set([chr(i) for i in range(2304, 2432)])
    # Create a set of Unicode code points for the characters in the title
    title_chars = set(list(title))
    # Return True if there is any overlap between the two sets
    return len(hindi_chars & title_chars) > 0

# Define a function to check a directory for HTML files with Hindi titles
def check_directory(directory):
    # Loop over all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is an HTML file
        if filename.endswith(".html"):
            # Open the file with codecs to ensure correct encoding
            with codecs.open(os.path.join(directory, filename), 'r', 'utf-8') as f:
                # Use BeautifulSoup to parse the HTML and extract the title
                soup = BeautifulSoup(f.read(), 'html.parser')
                title = soup.title.string
                # Check if the title contains any Hindi characters and print the result
                if is_hindi(title):
                    print("Hindi")
                else:
                    print("English")

# Call the check_directory function on a directory path
if __name__ == "__main__":
    check_directory("./www.classcentral.com")
