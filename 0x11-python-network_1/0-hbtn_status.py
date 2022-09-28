#!/usr/bin/python3
"""
fetch https://intranet.hbtn.io/status; display response
in tabulation
"""

import urllib.request

if __name__ == "__main__":
    urlPath = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(urlPath) as response:
        html = response.read()
        print('Body response:')
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
