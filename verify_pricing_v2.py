from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:8080')

        # Pricing Section
        pricing_section = page.locator('#pricing')
        pricing_section.screenshot(path='verification_pricing_v2.png')

        browser.close()

if __name__ == '__main__':
    run()
