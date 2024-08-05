#!/usr/bin/python3
'''
Script that takes 2 strings as arguments:
    - First argument is the name of the Markdown file
    - Second argument is the output file name
'''

import sys
import os.path


def main():
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)
    mdfile = sys.argv[1]
    htmlfile = sys.argv[2]

    if not os.path.isfile(mdfile):
        sys.stderr.write("Missing {}\n".format(mdfile))
        sys.exit(1)
    else:
        with open(mdfile, 'r') as f:
            content = f.read()
            with open(htmlfile, 'w') as file:
                file.write(content)
        sys.exit(0)


if __name__ == "__main__":
    main()
