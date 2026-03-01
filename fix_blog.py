import re

with open('blog/5-signs-you-need-a-virtual-assistant-2026/index.html', 'r') as f:
    content = f.read()

# Make sure we don't have duplicated or missing tags
content = content.replace("</div>", "</div>\n")
content = content.replace("</h1>", "</h1>\n")
content = content.replace("</h2>", "</h2>\n")
content = content.replace("</h3>", "</h3>\n")

with open('blog/5-signs-you-need-a-virtual-assistant-2026/index.html', 'w') as f:
    f.write(content)
