from bs4 import BeautifulSoup

with open('index.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Get footer
footer = soup.find('footer')
if footer:
    print("\n--- FOOTER EXISTS ---")
    print(str(footer)[:500] + "...")
else:
    print("\n--- FOOTER NOT FOUND ---")

# Inspect the parent element of a services__card
service_card = soup.find('div', class_='services__card')
if service_card:
    parent = service_card.parent
    print("\n--- SERVICES CARD PARENT ---")
    print(f"Parent element: {parent.name}")
    print(f"Parent classes: {parent.get('class', 'No class')}")

    grandparent = parent.parent
    if grandparent:
        print("\n--- SERVICES CARD GRANDPARENT ---")
        print(f"Grandparent element: {grandparent.name}")
        print(f"Grandparent classes: {grandparent.get('class', 'No class')}")

        main_text = grandparent.find('div', class_=lambda c: c and 'main-text' in c)
        if main_text:
            print("\n--- MAIN TEXT STRUCTURE ---")
            print(str(main_text))
