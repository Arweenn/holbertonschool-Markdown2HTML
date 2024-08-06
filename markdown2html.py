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
    ul_pattern = re.compile(r'^-\s+(.*)')
    ol_pattern = re.compile(r'^\*\s+(.*)')

    in_ul_list = False
    in_ol_list = False
    in_paragraph = False

    for line in lines:

        heading_match = heading_pattern.match(line)
        ul_match = ul_pattern.match(line)
        ol_match = ol_pattern.match(line)

        if heading_match:

            if in_ul_list:
                html_lines.append('</ul>')
                in_ul_list = False

            if in_ol_list:
                html_lines.append('</ol>')
                in_ol_list = False

            if in_paragraph:
                html_lines.append('</p>')
                in_paragraph = False

            heading_level = len(heading_match.group(1))
            heading_text = heading_match.group(2)
            html_lines.append(
                f'<h{heading_level}>{heading_text}</h{heading_level}>')

        elif ul_match:

            if in_ol_list:
                html_lines.append('</ol>')
                in_ol_list = False

            if in_paragraph:
                html_lines.append('</p>')
                in_paragraph = False

            if not in_ul_list:
                html_lines.append('<ul>')
                in_ul_list = True

            list_text = ul_match.group(1)
            html_lines.append(f'<li>{list_text}</li>')

        elif ol_match:

            if in_ul_list:
                html_lines.append('</ul>')
                in_ul_list = False

            if in_paragraph:
                html_lines.append('</p>')
                in_paragraph = False

            if not in_ol_list:
                html_lines.append('<ol>')
                in_ol_list = True

            list_text = ol_match.group(1)
            html_lines.append(f'<li>{list_text}</li>')

        else:

            if line.strip() == '':
                if in_paragraph:
                    html_lines.append('</p>')
                    in_paragraph = False
                continue

            if in_ul_list:
                html_lines.append('</ul>')
                in_ul_list = False

            if in_ol_list:
                html_lines.append('</ol>')
                in_ol_list = False

            if not in_paragraph:
                html_lines.append('<p>')
                in_paragraph = True

            if in_paragraph:
                if html_lines[-1] != '<p>':
                    html_lines.append('<br>')
                html_lines.append(f'{line}')

    if in_ul_list:
        html_lines.append('</ul>')

    if in_ol_list:
        html_lines.append('</ol>')

    if in_paragraph:
        html_lines.append('</p>')

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
