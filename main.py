from flask import Flask
app = Flask(__name__)

BASE_HTML = """
<html>
<head><title>INDEX</title></head>
<body>{}</body>
</html>
"""
HTML_ELEMENT = """
<button onclick="window.location='{}'" style="height: 120px; width: 210px; font-size: xx-large;">{}</button>
"""


def get_html():
    text = open('/etc/Caddyfile', 'r').read()

    urls = []
    for each in text.split('{\n    proxy')[:-1]:
        urls.append(each.split('\n\n')[-1].strip())

    elements = []
    for url in urls:
        elements.append(HTML_ELEMENT.format('https://{}'.format(url), url))

    inner_html = ''
    for element in elements:
        inner_html += element

    print(BASE_HTML.format(inner_html))


@app.route("/")
def html():
    return "Hello World!"
