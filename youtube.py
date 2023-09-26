#! /usr/bin/python3

import sys
import webbrowser

search = ' '.join(sys.argv[1:])

webbrowser.open(r'https://www.youtube.com/results?search_query=' + str(search))
