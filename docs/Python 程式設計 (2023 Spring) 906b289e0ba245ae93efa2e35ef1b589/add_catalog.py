import re, os, sys

re_catalog = re.compile(r"(?P<all><p id=\"(?P<id>[0-9a-zA-Z\-]+)\"[^>]*>\[目錄\]</p>)")
re_link = re.compile(r"(?P<all><h3 id=\"(?P<id>[0-9a-zA-Z\-]+)\"[^>]*>(?P<text>\[(?P<lable>[^\[\]]*)\].*?)(?=\<\/h3\>))")
re_prop = re.compile(r"(?P<all><table class=\"properties\"><tbody>.*</tbody></table>)")

t_catalog = "<div id=\"yang-id-001\" class=\"yang-class-001\">目 錄：</div>\n"
t_back    = "<a href=\"#yang-id-001\" class=\"yang-class-003\">回目錄</a>\n"


def main(name):
    fh = open(name,encoding="utf-8") 
    html = ""
    for line in fh:
        html+=line
    fh.close()
    ofn = name.replace(".html","-link.html")
    cata = t_catalog
    replaces = []
    if re_prop.findall(html):
        replaces = [(re_prop.findall(html)[0],"")]
    for m in re_link.findall(html):
        all = m[0]
        id = m[1]
        text = m[2]
        cata += f"<a href=\"#{id}\" class=\"yang-class-002\">{text}</a>\n"
        replaces.append((all,f"{t_back}{all}"))
    print(re_catalog.findall(html))
    replaces.append((re_catalog.findall(html)[0][0],cata))
    for t in replaces:
        html = html.replace(t[0],t[1])
    fh = open(ofn, 'w', encoding='UTF-8')
    fh.write(html)
    fh.close()    

if __name__=="__main__":
    if len(sys.argv)==2:
       main(sys.argv[1])
    else:
        print("\nUsage : fix_link.py <html-file-name>\n")
    