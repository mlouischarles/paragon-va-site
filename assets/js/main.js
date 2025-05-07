document.addEventListener('DOMContentLoaded', () => {
    console.log('content loaded');

    const menuToggler = document.querySelector('.nav__bar-menu-toggler');
    const menu = document.querySelector('.nav__bar-menu-small-screen');
    const navBar = document.querySelector('.nav__bar');
    const faqMap = document.querySelectorAll('.faq');

    var swiper = new Swiper('.testimonial-swiper', {
        loop: true,
        navigation: {
            nextEl: '.swiper-prev-slide',
            prevEl: '.swiper-next-slide'
        }
    });

    window.addEventListener('scroll', () => {
        if (window.scrollY > 10) {
            navBar.classList.add('nav__bar-scrolled');
        } else {
            navBar.classList.remove('nav__bar-scrolled');
        };
    });

    window.addEventListener('scroll', () => {
        menuToggler.querySelector('.icon-hamburger')
            .classList.remove('hidden');
        menuToggler.querySelector('.icon-x')
            .classList.add('hidden');
        if (menu.classList.contains("animate-fade-in-scrolled")) {
            menu.classList.remove("animate-fade-in-scrolled");
        } else if (menu.classList.contains("animate-fade-in")) {
            menu.classList.remove("animate-fade-in");
        };
    });

    menuToggler.addEventListener('click', function () {
        this.querySelector('.icon-hamburger')
            .classList.toggle('hidden');
        this.querySelector('.icon-x')
            .classList.toggle('hidden');
        if (window.scrollY > 10) {
            menu.classList.toggle('animate-fade-in-scrolled');
        } else {
            menu.classList.toggle('animate-fade-in');
        };
    });

    function toggleFAQ(clickedButton, id) {
        const faqItems = document.querySelectorAll('[data-faq-id]');
        let shouldExpandTarget = true;
    
        // First pass: determine if the clicked one is already expanded
        faqItems.forEach(item => {
          if (item.dataset.faqId === id) {
            const btn = item.querySelector('.toggler');
            shouldExpandTarget = btn.getAttribute("aria-expanded") !== "true";
          }
        });
    
        // Second pass: collapse all, then optionally expand clicked one
        faqItems.forEach(item => {
          const btn = item.querySelector('.toggler');
          const content = item.querySelector('.faq-content');
          const icon = item.querySelector('.down-chevron');
    
          const isTarget = item.dataset.faqId === id;
    
          if (btn && content && icon) {
            btn.setAttribute("aria-expanded", "false");
            content.classList.remove('faq-padding');
            content.style.maxHeight = "0";
            icon.classList.remove("up-chevron");
    
            // Expand only the target item if needed
            if (isTarget && shouldExpandTarget) {
              btn.setAttribute("aria-expanded", "true");
              content.classList.add('faq-padding');
              content.style.maxHeight = content.scrollHeight + "px";
              icon.classList.add("up-chevron");
            }
          }
        });
    };

    faqMap.forEach((faq, i) => {
        faq.dataset.faqId = `faq-${i}`;
        const button = faq.querySelector('.toggler');
        const faqId = `faq-${i}`;

        button.addEventListener('click', () => {
            toggleFAQ(faq, faqId);
        });
    });
});