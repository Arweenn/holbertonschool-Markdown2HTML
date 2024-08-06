#!/usr/bin/python3
'''
Script that takes 2 strings as arguments:
    - First argument is the name of the Markdown file
    - Second argument is the output file name
'''

import sys
import os.path
import re


def convert_markdown_to_html(md_content):

    lines = md_content.split('\n')
    html_lines = []

    heading_pattern = re.compile(r'^(#{1,6})\s*(.*)')
    list_pattern = re.compile(r'^-\s+(.*)')
    in_list = False

    for line in lines:

        heading_match = heading_pattern.match(line)
        list_match = list_pattern.match(line)

        if heading_match:

            if in_list:
                html_lines.append('</ul>')
                in_list = False

            heading_level = len(heading_match.group(1))
            heading_text = heading_match.group(2)
            html_lines.append(
                f'<h{heading_level}>{heading_text}</h{heading_level}>')

        elif list_match:

            if not in_list:
                html_lines.append(f'<ul>')
                in_list = True

            list_text = list_match.group(1)
            html_lines.append(f'<li>{list_text}</li>')

        else:
            if in_list:
                html_lines.append('</ul>')
                in_list = False

    if in_list:
        html_lines.append('</ul>')

    html_text = '\n'.join(html_lines)
    return html_text


def main():

    if len(sys.argv) != 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    mdfile = sys.argv[1]
    htmlfile = sys.argv[2]

    if not os.path.isfile(mdfile):
        sys.stderr.write("Missing {}\n".format(mdfile))
        sys.exit(1)

    with open(mdfile, 'r', encoding='utf-8') as f:
        content = f.read()

    html_content = convert_markdown_to_html(content)

    with open(htmlfile, 'w', encoding='utf-8') as file:
        file.write(html_content + '\n')

    sys.exit(0)


if __name__ == "__main__":
    main()
