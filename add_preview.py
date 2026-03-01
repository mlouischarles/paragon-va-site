from bs4 import BeautifulSoup

with open('index.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

new_section_html = """
<section class="services__section section-padding">
    <div class="container services__container">
        <div class="services__main-text">
            <h2 class="main-heading">
                Latest from Our Blog
            </h2>
        </div>
        <div class="services__card-wrapper" style="grid-template-columns: 1fr; margin-top: 40px; display: grid;">
            <div class="services__card" style="max-width: 800px; margin: 0 auto; padding: 40px;">
                <div class="card-header">
                    <h3 class="heading" style="font-size: 1.5rem; margin-bottom: 15px;">5 Signs You Need to Hire a Virtual Assistant in 2026</h3>
                </div>
                <div class="card-body">
                    <p class="desc" style="font-size: 1.1rem; line-height: 1.6;">
                        If you're constantly playing catch-up, struggling to focus on high-value work, or watching important tasks slip through the cracks, it might be time to consider hiring a virtual assistant. Here are five clear signs that your business is ready for VA support.
                    </p>
                    <a href="/blog/5-signs-you-need-a-virtual-assistant-2026/" class="btn" style="display: inline-block; margin-top: 25px;">Read More →</a>
                </div>
            </div>
        </div>
    </div>
</section>
"""

new_section = BeautifulSoup(new_section_html, 'html.parser')

testimonials = soup.find('section', id='testimonials')
if testimonials:
    testimonials.insert_after(new_section)
    print("Inserted new section after testimonials.")
else:
    print("Could not find testimonials section.")

with open('index.html', 'w') as f:
    f.write(str(soup))
