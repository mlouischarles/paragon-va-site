from bs4 import BeautifulSoup

with open('index.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

for a in soup.find_all('a', href=True):
    if a['href'] == '/blog':
        a['href'] = '/blog/5-signs-you-need-a-virtual-assistant-2026/'

with open('index.html', 'w') as f:
    f.write(str(soup))
