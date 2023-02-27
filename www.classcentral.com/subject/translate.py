from bs4 import BeautifulSoup
from googletrans import Translator
import os

for item in os.listdir('.'):
    if item.endswith('.html'):
        if item == 'trigonometry.html' or item == 'urban-planning.html' or item == 'veterinary-science.html' or item=='visual-arts.html' or item=='web-design.html' or item=='web-development.html':
            # Load the HTML file
            with open(item, 'r',encoding='utf-8') as f:
                html_text = f.read()

            # # Parse the HTML file
            soup = BeautifulSoup(html_text, 'html.parser')

            # # Initialize the translator
            translator = Translator(service_urls=['translate.googleapis.com'])

            print(item)
            # Find all the text in the HTML file
            for tag in soup.find_all(text=True):
                # Ignore script and style tags
                if tag.parent.name in ['script', 'style']:
                    continue

                # Check if the text is empty or whitespace-only
                if not tag.strip():
                    continue


                if tag == 'html':
                    continue

                # if translator.detect(tag).lang == 'hi' and tag.name == 'title':
                #     print(tag)
                #     print('ALREADY TRANSLATED')
                #     break
                # Translate the text using Googletrans
                translated_text = translator.translate(tag, src='en', dest='hi').text
                print(translated_text)

                # Replace the original text with the translated text
                tag.replace_with(translated_text)

            # Write the translated HTML to a new file
            with open(item, 'w', encoding='utf-8') as f:
                f.write(str(soup))
