# app.py - Complete Portfolio Website using Reflax (Python Frontend Framework)
# Run with: python app.py
# Then open http://localhost:5000

from reflax import Reflax, html, useState, useEffect
import random
import time

app = Reflax(__name__)

# ============= QUOTES DATABASE =============
QUOTES = [
    {"text": "The best way to predict the future is to invent it.", "author": "Alan Kay"},
    {"text": "Strive not to be a success, but rather to be of value.", "author": "Albert Einstein"},
    {"text": "Innovation distinguishes between a leader and a follower.", "author": "Steve Jobs"},
    {"text": "Don't watch the clock; do what it does. Keep going.", "author": "Sam Levenson"},
    {"text": "Success is not in what you have, but who you are.", "author": "Bo Bennett"},
    {"text": "Your time is limited, so don't waste it living someone else's life.", "author": "Steve Jobs"},
    {"text": "The harder you work for something, the greater you'll feel when you achieve it.", "author": "Unknown"},
    {"text": "Dream bigger. Do bigger.", "author": "Unknown"},
    {"text": "Don't stop when you're tired. Stop when you're done.", "author": "Unknown"},
    {"text": "Little things make big days.", "author": "Unknown"},
    {"text": "It always seems impossible until it's done.", "author": "Nelson Mandela"},
    {"text": "Don't wait for opportunity. Create it.", "author": "Unknown"},
    {"text": "Sometimes we're tested not to show our weaknesses, but to discover our strengths.", "author": "Unknown"},
    {"text": "The key to success is to focus on goals, not obstacles.", "author": "Unknown"},
    {"text": "Push yourself, because no one else is going to do it for you.", "author": "Unknown"},
    {"text": "Great things never come from comfort zones.", "author": "Unknown"},
    {"text": "Action is the foundational key to all success.", "author": "Pablo Picasso"},
    {"text": "Start where you are. Use what you have. Do what you can.", "author": "Arthur Ashe"},
    {"text": "Work hard in silence, let your success be your noise.", "author": "Frank Ocean"},
    {"text": "Success usually comes to those who are too busy to be looking for it.", "author": "Henry David Thoreau"},
]

# ============= COMPONENTS =============

def QuoteBanner():
    """Typing animation quote banner component"""
    quote_text, set_quote_text = useState('')
    quote_author, set_quote_author = useState('')
    char_index, set_char_index = useState(0)
    current_quote_obj, set_current_quote_obj = useState(None)
    is_typing, set_is_typing = useState(True)
    
    def select_random_quote():
        return random.choice(QUOTES)
    
    def type_quote():
        obj = current_quote_obj
        if obj and char_index < len(obj['text']):
            set_quote_text(quote_text + obj['text'][char_index])
            set_char_index(char_index + 1)
            return True
        return False
    
    def erase_quote():
        if char_index > 0:
            set_quote_text(quote_text[:-1])
            set_char_index(char_index - 1)
            return True
        return False
    
    def start_new_quote():
        new_quote = select_random_quote()
        set_current_quote_obj(new_quote)
        set_quote_author(f"— {new_quote['author']}")
        set_quote_text('')
        set_char_index(0)
        set_is_typing(True)
    
    useEffect(lambda: start_new_quote(), [])
    
    # Typing animation effect
    def animate():
        if is_typing:
            if not type_quote():
                set_is_typing(False)
        else:
            # Pause then erase
            import threading
            def erase_after_pause():
                time.sleep(3)
                # Use a flag to erase
                nonlocal is_typing
                pass
    
    useEffect(lambda: animate(), [quote_text, is_typing, char_index])
    
    return html.div(
        {'className': 'quotes-container'},
        html.span({'id': 'quote-text'}, quote_text),
        html.span({'id': 'quote-author'}, quote_author)
    )


def Navigation():
    """Navigation bar component"""
    current_page, set_current_page = useState('home')
    
    # Expose setter globally for nav clicks
    def navigate(page):
        set_current_page(page)
    
    # Store in window for child components
    useEffect(lambda: setattr(__builtins__, '_nav_setter', navigate), [])
    
    nav_links = ['home', 'about', 'services', 'contacts']
    return html.div(
        {'className': 'header'},
        *[html.a(
            {
                'className': 'nav-link',
                'onClick': lambda p=page: set_current_page(p),
                'key': page
            },
            page
        ) for page in nav_links]
    )


def HomePage():
    """Home page with profile picture and welcome typing effect"""
    welcome_text, set_welcome_text = useState('')
    welcome_index, set_welcome_index = useState(0)
    full_welcome = 'Welcome to My Portfolio'
    
    def type_welcome():
        if welcome_index < len(full_welcome):
            set_welcome_text(welcome_text + full_welcome[welcome_index])
            set_welcome_index(welcome_index + 1)
    
    useEffect(lambda: type_welcome(), [welcome_index])
    
    return html.div(
        {'className': 'page-container'},
        html.img({
            'src': 'https://i.postimg.cc/MHFHR44R/pic.jpg',
            'alt': 'Profile Picture',
            'className': 'picture'
        }),
        html.span({'id': 'welcome-text'}, welcome_text),
        html.div({'className': 'cards-container'},
            html.div({'className': 'card'},
                html.h1({}, 'I am Tole Caxtone Kirigha'),
                html.p({}, 'Passionate about technology and innovation, I am a developer crafting solutions that blend creativity with functionality. Explore my projects, skills, and services that showcase my expertise in web and mobile development.'),
                html.p({'className': 'italic'}, "Let's build something amazing together!")
            ),
            html.div({'className': 'card indent-right'},
                html.h2({}, 'My Expertise'),
                html.ul({'className': 'skills-list'},
                    html.li({}, 'Mobile Development'),
                    html.li({}, 'Web Development'),
                    html.li({}, 'Artificial Intelligence & Machine Learning'),
                    html.li({}, 'Internet of Things (IoT)'),
                    html.li({}, 'Robotics')
                )
            )
        )
    )


def AboutPage():
    """About Me page"""
    return html.div(
        {'className': 'page-container'},
        html.div({'className': 'card'},
            html.h1({}, 'About Me'),
            html.p({}, 'I am Tole Caxtone Kirigha, a passionate developer and technology enthusiast. I specialize in combining creativity with technical expertise to build innovative solutions.'),
            html.p({}, 'With experience in mobile and web development, AI & Machine Learning, IoT, and robotics, I continuously strive to expand my skills and deliver impactful projects.'),
            html.p({'className': 'italic'}, 'Thank you for visiting my portfolio!')
        )
    )


def ServicesPage():
    """Services page"""
    return html.div(
        {'className': 'page-container'},
        html.div({'className': 'card'},
            html.h1({}, 'Services I Offer'),
            html.ul({'className': 'skills-list'},
                html.li({}, 'Mobile App Development (React Native & Expo)'),
                html.li({}, 'Web Development (React, Flask)'),
                html.li({}, 'AI & Machine Learning Solutions'),
                html.li({}, 'IoT Integration and Development'),
                html.li({}, 'Robotics Prototyping and Programming')
            )
        )
    )


def ContactPage():
    """Contact page with social links"""
    return html.div(
        {'className': 'page-container'},
        html.div({'className': 'card'},
            html.h1({}, 'Contact Me'),
            html.ul({'className': 'contact-list'},
                html.li({}, 'GitHub: ', html.a({'href': 'https://github.com/ToleInventor', 'target': '_blank', 'className': 'contact-link'}, 'ToleInventor')),
                html.li({}, 'WhatsApp / Calls: ', html.a({'href': 'tel:+254742174250', 'className': 'contact-link'}, '0742174250')),
                html.li({}, 'TikTok: ', html.a({'href': 'https://www.tiktok.com/@caxtonetechkenya', 'target': '_blank', 'className': 'contact-link'}, '@caxtonetechkenya')),
                html.li({}, 'YouTube: ', html.a({'href': 'https://www.youtube.com/@CaxtoneTechKenya', 'target': '_blank', 'className': 'contact-link'}, '@CaxtoneTechKenya')),
                html.li({}, 'Twitter: ', html.a({'href': 'https://twitter.com/DevTole', 'target': '_blank', 'className': 'contact-link'}, 'DevTole')),
                html.li({}, 'Kaggle: ', html.a({'href': 'https://www.kaggle.com/ToleInventor', 'target': '_blank', 'className': 'contact-link'}, 'ToleInventor'))
            )
        )
    )


# ============= MAIN APP COMPONENT =============

def App():
    """Main application component with routing"""
    current_page, set_current_page = useState('home')
    
    # Page mapping
    pages = {
        'home': HomePage,
        'about': AboutPage,
        'services': ServicesPage,
        'contacts': ContactPage
    }
    
    # Override navigation from children
    def navigate(page):
        set_current_page(page)
    
    # Create navigation with context
    nav_links = ['home', 'about', 'services', 'contacts']
    
    CurrentPageComponent = pages.get(current_page, HomePage)
    
    return html.div(
        {'className': 'app-container'},
        # Global styles
        html.style('''
            :root {
                --text-color: #1B263B;
                --background-color: #EBF5FB;
                --accent-color: #4A90E2;
                --card-bg: #FFFFFF;
                --card-shadow: rgba(0, 0, 0, 0.1);
            }
            body {
                background-color: var(--background-color);
                margin: 0;
                font-family: 'Roboto', sans-serif;
                color: var(--text-color);
            }
            .quotes-container {
                background-color: var(--accent-color);
                color: white;
                font-style: italic;
                font-weight: 600;
                padding: 12px 20px;
                text-align: center;
                font-size: 1.15rem;
                user-select: none;
                min-height: 85px;
            }
            #quote-text {
                display: inline;
            }
            #quote-author {
                display: block;
                text-align: right;
                margin-top: 5px;
                font-style: italic;
                font-weight: 400;
                font-size: 1rem;
                opacity: 0.85;
            }
            .header {
                display: flex;
                justify-content: flex-end;
                padding: 10px 20px;
                background: var(--card-bg);
                box-shadow: 0 2px 5px var(--card-shadow);
                position: sticky;
                top: 0;
                z-index: 1000;
            }
            .nav-link {
                color: var(--text-color);
                padding: 0 15px;
                text-decoration: none;
                font-weight: 500;
                transition: all 0.3s ease;
                cursor: pointer;
            }
            .nav-link:hover {
                font-family: 'Pacifico', cursive;
                animation: colorShift 2s infinite alternate;
                color: var(--accent-color);
            }
            .card {
                background: var(--card-bg);
                max-width: 700px;
                margin: 40px auto;
                border-radius: 15px;
                box-shadow: 0 6px 20px var(--card-shadow);
                padding: 40px 40px 50px 40px;
                transition: box-shadow 0.3s ease;
                cursor: default;
            }
            .card:hover {
                box-shadow: 0 8px 30px rgba(74, 144, 226, 0.5);
            }
            .card h1, .card h2 {
                color: var(--accent-color);
                margin-bottom: 20px;
                transition: color 0.3s ease;
            }
            .card p {
                font-size: 1.18rem;
                line-height: 1.7;
                margin: 15px 0;
                color: var(--text-color);
            }
            .card p.italic {
                font-size: 1rem;
                font-style: italic;
                margin-top: 30px;
            }
            @keyframes colorShift {
                0% { color: #4A90E2; }
                25% { color: #357ABD; }
                50% { color: #1C5FA8; }
                75% { color: #4A90E2; }
                100% { color: #357ABD; }
            }
            .picture {
                display: block;
                margin: 25px auto 5px auto;
                width: 200px;
                height: 200px;
                border-radius: 50%;
                object-fit: cover;
                border: 4px solid var(--accent-color);
                box-shadow: 0 4px 10px var(--card-shadow);
            }
            #welcome-text {
                display: block;
                text-align: center;
                margin: 15px 0 35px 0;
                font-size: 1.8rem;
                font-weight: 600;
                color: var(--accent-color);
                font-family: 'Roboto', sans-serif;
                white-space: nowrap;
                overflow: hidden;
                border-right: 0.1em solid var(--accent-color);
                animation: blinkCursor 0.8s step-end infinite;
            }
            @keyframes blinkCursor {
                50% { border-color: transparent; }
            }
            .cards-container {
                max-width: 900px;
                margin: 20px auto 60px auto;
                display: flex;
                gap: 40px;
                justify-content: flex-start;
                flex-wrap: wrap;
            }
            .indent-right {
                margin-left: 0;
            }
            @media (min-width: 768px) {
                .indent-right {
                    margin-left: 40px;
                }
            }
            .skills-list {
                list-style-type: none;
                padding: 0;
                font-size: 1.15rem;
            }
            .skills-list li {
                margin: 8px 0;
                padding-left: 1.1em;
                position: relative;
            }
            .skills-list li::before {
                content: '•';
                position: absolute;
                left: 0;
                color: var(--accent-color);
                font-weight: bold;
            }
            .contact-list {
                list-style: none;
                padding-left: 0;
                font-size: 1.2rem;
            }
            .contact-list li {
                margin: 12px 0;
            }
            .contact-link {
                color: var(--accent-color);
                text-decoration: none;
                font-weight: 600;
                transition: color 0.3s ease;
            }
            .contact-link:hover {
                color: var(--text-color);
                font-family: 'Pacifico', cursive;
                animation: colorShift 2s infinite alternate;
            }
            .page-container {
                min-height: calc(100vh - 180px);
            }
        '''),
        
        # Quote banner with typing animation
        html.div({'className': 'quotes-container'},
            html.span({'id': 'quote-text'}, ''),
            html.span({'id': 'quote-author'}, '')
        ),
        
        # Navigation
        html.div({'className': 'header'},
            *[html.a({'className': 'nav-link', 'onClick': lambda p=page: set_current_page(p), 'key': page}, page.capitalize() if page != 'home' else 'Home') 
              for page in ['home', 'about', 'services', 'contacts']]
        ),
        
        # Dynamic page content
        CurrentPageComponent(),
        
        # JavaScript for quote typing animation (since Reflax needs imperative animation)
        html.script('''
            // Quote typing animation (independent of Reflax state for smooth effect)
            const quotesList = [
                { text: "The best way to predict the future is to invent it.", author: "Alan Kay" },
                { text: "Strive not to be a success, but rather to be of value.", author: "Albert Einstein" },
                { text: "Innovation distinguishes between a leader and a follower.", author: "Steve Jobs" },
                { text: "Don't watch the clock; do what it does. Keep going.", author: "Sam Levenson" },
                { text: "Success is not in what you have, but who you are.", author: "Bo Bennett" },
                { text: "Your time is limited, so don't waste it living someone else's life.", author: "Steve Jobs" },
                { text: "The harder you work for something, the greater you'll feel when you achieve it.", author: "Unknown" },
                { text: "Dream bigger. Do bigger.", author: "Unknown" },
                { text: "Don't stop when you're tired. Stop when you're done.", author: "Unknown" },
                { text: "Little things make big days.", author: "Unknown" },
                { text: "It always seems impossible until it's done.", author: "Nelson Mandela" },
                { text: "Don't wait for opportunity. Create it.", author: "Unknown" },
                { text: "Sometimes we're tested not to show our weaknesses, but to discover our strengths.", author: "Unknown" },
                { text: "The key to success is to focus on goals, not obstacles.", author: "Unknown" },
                { text: "Push yourself, because no one else is going to do it for you.", author: "Unknown" },
                { text: "Great things never come from comfort zones.", author: "Unknown" },
                { text: "Action is the foundational key to all success.", author: "Pablo Picasso" }
            ];
            
            const quoteElement = document.getElementById('quote-text');
            const authorElement = document.getElementById('quote-author');
            let charIndex = 0;
            let currentQuote = '';
            let typingSpeed = 50;
            let pauseBetweenQuotes = 4000;
            let isTyping = true;
            let timeoutId = null;
            
            function typeQuote() {
                if (charIndex < currentQuote.length) {
                    quoteElement.textContent += currentQuote.charAt(charIndex);
                    charIndex++;
                    timeoutId = setTimeout(typeQuote, typingSpeed);
                } else {
                    timeoutId = setTimeout(() => {
                        eraseQuote();
                    }, pauseBetweenQuotes);
                }
            }
            
            function eraseQuote() {
                if (charIndex > 0) {
                    quoteElement.textContent = currentQuote.substring(0, charIndex - 1);
                    charIndex--;
                    timeoutId = setTimeout(eraseQuote, typingSpeed / 2);
                } else {
                    displayNewQuote();
                }
            }
            
            function displayNewQuote() {
                const randomIndex = Math.floor(Math.random() * quotesList.length);
                currentQuote = `"${quotesList[randomIndex].text}"`;
                authorElement.textContent = `— ${quotesList[randomIndex].author}`;
                charIndex = 0;
                quoteElement.textContent = '';
                typeQuote();
            }
            
            // Welcome text typing animation for home page
            function initWelcomeTyping() {
                const welcomeEl = document.getElementById('welcome-text');
                if (!welcomeEl) return;
                const fullText = 'Welcome to My Portfolio';
                let i = 0;
                welcomeEl.textContent = '';
                function typeWelcome() {
                    if (i < fullText.length) {
                        welcomeEl.textContent += fullText.charAt(i);
                        i++;
                        setTimeout(typeWelcome, 100);
                    } else {
                        welcomeEl.style.borderRight = 'none';
                    }
                }
                typeWelcome();
            }
            
            // Start quote animation
            displayNewQuote();
            
            // Observe for home page navigation to restart welcome typing
            const observer = new MutationObserver(function(mutations) {
                mutations.forEach(function(mutation) {
                    if (mutation.type === 'childList') {
                        const welcomeEl = document.getElementById('welcome-text');
                        if (welcomeEl && welcomeEl.textContent === '') {
                            initWelcomeTyping();
                        }
                    }
                });
            });
            observer.observe(document.body, { childList: true, subtree: true });
            
            // Also run on initial load if home is active
            setTimeout(initWelcomeTyping, 100);
        ''')
    )


# ============= RUN APPLICATION =============

if __name__ == '__main__':
    print("=" * 50)
    print("🌟 Reflax Portfolio Website")
    print("=" * 50)
    print("📱 Portfolio by Tole Caxtone Kirigha")
    print("🚀 Starting server at http://localhost:5000")
    print("📄 Pages: Home, About, Services, Contacts")
    print("💡 Press Ctrl+C to stop the server")
    print("=" * 50)
    
    app.run(host='0.0.0.0')
