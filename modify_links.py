from bs4 import BeautifulSoup

with open('blog/5-signs-you-need-a-virtual-assistant-2026/index.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Update header links
header = soup.find('header')
if header:
    for a in header.find_all('a', href=True):
        href = a['href']
        if href.startswith('#'):
            a['href'] = '/' + href
        elif href == '/blog':
            a['href'] = '/blog/5-signs-you-need-a-virtual-assistant-2026/'
        elif 'calendly.com' in href:
            a['href'] = 'https://calendly.com/hireparagonva-info'

# Update footer links
footer = soup.find('footer')
if footer:
    for a in footer.find_all('a', href=True):
        href = a['href']
        if href.startswith('#'):
            a['href'] = '/' + href
        elif 'calendly.com' in href:
            a['href'] = 'https://calendly.com/hireparagonva-info'

    # Check and update address
    address_p = footer.find(lambda tag: tag.name == 'p' and 'Boston' in tag.text)
    if address_p:
        address_p.string = '265 Franklin Street\nBoston, MA 02110'
        # Make sure <br> is preserved
        address_p.clear()
        address_p.append('265 Franklin Street')
        address_p.append(soup.new_tag('br'))
        address_p.append('Boston, MA 02110')

# Update Calendly links in main
main = soup.find('main')
if main:
    for a in main.find_all('a', href=True):
        if 'calendly.com' in a['href']:
            a['href'] = 'https://calendly.com/hireparagonva-info'

with open('blog/5-signs-you-need-a-virtual-assistant-2026/index.html', 'w') as f:
    f.write(str(soup))

print("Links updated successfully.")
