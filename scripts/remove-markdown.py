#!/usr/bin/env python
from __future__ import print_function
from pandocfilters import toJSONFilter
import re
import sys

"""
Remove MARKDOWNBLOCK
"""

incomment = False


def comment(k, v, fmt, meta):
    global incomment

    if k == 'RawBlock':
        fmt, s = v
        if re.search("<!-- BEGIN MARKDOWNBLOCK -->", s):
            incomment = True
        elif re.search("<!-- END MARKDOWNBLOCK -->", s):
            incomment = False
    if incomment:
        return []  # suppress anything in this block

if __name__ == "__main__":
    toJSONFilter(comment)

