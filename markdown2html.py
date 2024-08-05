#!/usr/bin/python3
'''
Script that takes 2 strings as arguments:
    - First argument is the name of the Markdown file
    - Second argument is the output file name
'''

import sys
import os
import markdown


def markdown2html():

    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html")
        exit(1)

    input_md = sys.argv[1]
    output_html = sys.argv[2]

    if not os.path.exists(sys.argv[1]):
        print("Missing " + input_md + "\n")
        exit(1)

    with open(input_md, 'r', encoding='utf-8') as f:
        md_content = f.read()

    html_content = markdown.markdown(md_content)

    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(html_content)

    exit(0)


if __name__ == "__main__":
    markdown2html()
