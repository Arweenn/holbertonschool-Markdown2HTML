#!/usr/bin/python3
'''
Script that takes 2 strings as arguments:
    - First argument is the name of the Markdown file
    - Second argument is the output file name
'''

import sys
import os


def markdown2html(input_md, output_html):

    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    elif not os.path.exists(sys.argv[1]):
        sys.stderr.write("Missing " + input_md + "\n")
        sys.exit(1)
