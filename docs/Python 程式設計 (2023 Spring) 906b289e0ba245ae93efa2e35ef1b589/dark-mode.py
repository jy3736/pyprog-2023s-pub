#! /usr/bin/python

import sys, os

add_to_head='<link rel="stylesheet" href="dark-theme.css"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.5.0/styles/github-dark-dimmed.min.css"><script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.5.0/highlight.min.js"></script>'

add_to_body="""
<script>hljs.highlightAll();</script>
"""

yt1 = '[教學影片]：'
yt2 = '<img src="img/yang.png" width="100px">'


def main(name):
    ofn = name.replace(".html","-dark.html")
    fh = open(name,encoding="utf-8") 
    text = ""
    for l in fh:
        text+=l
    text = text.replace("</head",add_to_head + '</head')
    text = text.replace("</body",add_to_body + '</body')
    text = text.replace('href="https:',' target="_blank" href="https:')    
    text = text.replace(yt1,yt2)
    dark = open(ofn, 'w', encoding='UTF-8')
    dark.write(text)
    dark.close()
    fh.close()
    
if __name__=="__main__":
    if len(sys.argv)==2:
        main(sys.argv[1])
    else:
        print("\nUsage : add_catalog.py <html-file-name>\n")
