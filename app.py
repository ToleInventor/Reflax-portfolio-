"""Complete Portfolio Website using Reflex Framework"""

import reflex as rx
import random
from datetime import datetime

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
    {"text": "Success is what happens after you have survived all your mistakes.", "author": "Anora Lee"},
    {"text": "Action is the foundational key to all success.", "author": "Pablo Picasso"},
    {"text": "Start where you are. Use what you have. Do what you can.", "author": "Arthur Ashe"},
    {"text": "The secret of getting ahead is getting started.", "author": "Mark Twain"},
    {"text": "Work hard in silence, let your success be your noise.", "author": "Frank Ocean"},
    {"text": "Success usually comes to those who are too busy to be looking for it.", "author": "Henry David Thoreau"},
    {"text": "Don't be afraid to give up the good to go for the great.", "author": "John D. Rockefeller"},
    {"text": "I find that the harder I work, the more luck I seem to have.", "author": "Thomas Jefferson"},
    {"text": "Opportunities don't happen. You create them.", "author": "Chris Grosser"},
    {"text": "Dream it. Wish it. Do it.", "author": "Unknown"},
    {"text": "Success is not the key to happiness. Happiness is the key to success.", "author": "Albert Schweitzer"},
    {"text": "Hard work beats talent when talent doesn't work hard.", "author": "Tim Notke"}
]

# ============= STATE MANAGEMENT =============

class State(rx.State):
    """App state management"""
    current_page: str = "home"
    quote_text: str = ""
    quote_author: str = ""
    quote_index: int = 0
    typing_char_index: int = 0
    is_typing: bool = True
    welcome_text: str = ""
    welcome_index: int = 0
    
    def __init__(self):
        super().__init__()
        self.load_random_quote()
    
    def load_random_quote(self):
        """Load a random quote from the database"""
        quote = random.choice(QUOTES)
        self.quote_text = f'"{quote["text"]}"'
        self.quote_author = f"— {quote['author']}"
        self.typing_char_index = len(self.quote_text)
    
    def navigate_to(self, page: str):
        """Navigate between pages"""
        self.current_page = page
    
    def type_welcome(self):
        """Typing animation for welcome text"""
        full_text = "Welcome to My Portfolio"
        if self.welcome_index < len(full_text):
            self.welcome_text += full_text[self.welcome_index]
            self.welcome_index += 1
            return True
        return False


# ============= COMPONENTS =============

def navbar():
    """Navigation bar component"""
    return rx.hstack(
        rx.hstack(
            rx.link(
                "Home",
                on_click=lambda: State.navigate_to("home"),
                class_name="nav-link",
            ),
            rx.link(
                "About",
                on_click=lambda: State.navigate_to("about"),
                class_name="nav-link",
            ),
            rx.link(
                "Services",
                on_click=lambda: State.navigate_to("services"),
                class_name="nav-link",
            ),
            rx.link(
                "Contacts",
                on_click=lambda: State.navigate_to("contacts"),
                class_name="nav-link",
            ),
            spacing="4",
            justify="end",
            width="100%",
        ),
        class_name="header",
    )


def quote_banner():
    """Quote banner with typing animation"""
    return rx.vstack(
        rx.text(
            State.quote_text,
            id="quote-text",
            class_name="quote-text",
        ),
        rx.text(
            State.quote_author,
            id="quote-author",
            class_name="quote-author",
        ),
        class_name="quotes-container",
    )


def home_page():
    """Home page component"""
    return rx.vstack(
        rx.image(
            src="https://i.postimg.cc/MHFHR44R/pic.jpg",
            class_name="picture",
            alt="Profile Picture",
        ),
        rx.text(
            State.welcome_text,
            id="welcome-text",
            class_name="welcome-text",
        ),
        rx.hstack(
            rx.card(
                rx.vstack(
                    rx.heading("I am Tole Caxtone Kirigha", size="lg"),
                    rx.text(
                        "Passionate about technology and innovation, I am a developer "
                        "crafting solutions that blend creativity with functionality. "
                        "Explore my projects, skills, and services that showcase my "
                        "expertise in web and mobile development."
                    ),
                    rx.text(
                        "Let's build something amazing together!",
                        class_name="italic",
                    ),
                    spacing="4",
                    align="start",
                ),
                class_name="card",
            ),
            rx.card(
                rx.vstack(
                    rx.heading("My Expertise", size="md"),
                    rx.list.unordered(
                        rx.list.item("Mobile Development"),
                        rx.list.item("Web Development"),
                        rx.list.item("Artificial Intelligence & Machine Learning"),
                        rx.list.item("Internet of Things (IoT)"),
                        rx.list.item("Robotics"),
                        class_name="skills-list",
                    ),
                    spacing="4",
                ),
                class_name="card indent-right",
            ),
            spacing="8",
            class_name="cards-container",
            flex_wrap="wrap",
        ),
        spacing="4",
        width="100%",
    )


def about_page():
    """About page component"""
    return rx.card(
        rx.vstack(
            rx.heading("About Me", size="lg"),
            rx.text(
                "I am Tole Caxtone Kirigha, a passionate developer and technology "
                "enthusiast. I specialize in combining creativity with technical "
                "expertise to build innovative solutions."
            ),
            rx.text(
                "With experience in mobile and web development, AI & Machine Learning, "
                "IoT, and robotics, I continuously strive to expand my skills and "
                "deliver impactful projects."
            ),
            rx.text(
                "Thank you for visiting my portfolio!",
                class_name="italic",
            ),
            spacing="4",
            align="start",
        ),
        class_name="card",
    )


def services_page():
    """Services page component"""
    return rx.card(
        rx.vstack(
            rx.heading("Services I Offer", size="lg"),
            rx.list.unordered(
                rx.list.item("Mobile App Development (React Native & Expo)"),
                rx.list.item("Web Development (React, Flask)"),
                rx.list.item("AI & Machine Learning Solutions"),
                rx.list.item("IoT Integration and Development"),
                rx.list.item("Robotics Prototyping and Programming"),
                class_name="skills-list",
            ),
            spacing="4",
            align="start",
        ),
        class_name="card",
    )


def contact_page():
    """Contact page component"""
    return rx.card(
        rx.vstack(
            rx.heading("Contact Me", size="lg"),
            rx.vstack(
                rx.link(
                    "GitHub: ToleInventor",
                    href="https://github.com/ToleInventor",
                    is_external=True,
                    class_name="contact-link",
                ),
                rx.link(
                    "WhatsApp / Calls: 0742174250",
                    href="tel:+254742174250",
                    class_name="contact-link",
                ),
                rx.link(
                    "TikTok: @caxtonetechkenya",
                    href="https://www.tiktok.com/@caxtonetechkenya",
                    is_external=True,
                    class_name="contact-link",
                ),
                rx.link(
                    "YouTube: @CaxtoneTechKenya",
                    href="https://www.youtube.com/@CaxtoneTechKenya",
                    is_external=True,
                    class_name="contact-link",
                ),
                rx.link(
                    "Twitter: DevTole",
                    href="https://twitter.com/DevTole",
                    is_external=True,
                    class_name="contact-link",
                ),
                rx.link(
                    "Kaggle: ToleInventor",
                    href="https://www.kaggle.com/ToleInventor",
                    is_external=True,
                    class_name="contact-link",
                ),
                spacing="3",
                align="start",
            ),
            spacing="4",
            align="start",
        ),
        class_name="card",
    )


def render_page():
    """Render the appropriate page based on current state"""
    return rx.cond(
        State.current_page == "home",
        home_page(),
        rx.cond(
            State.current_page == "about",
            about_page(),
            rx.cond(
                State.current_page == "services",
                services_page(),
                contact_page(),
            ),
        ),
    )


# ============= MAIN APP =============

def index() -> rx.Component:
    """Main application component"""
    return rx.container(
        # Global styles
        rx.style("""
            :root {
                --text-color: #1B263B;
                --background-color: #EBF5FB;
                --accent-color: #4A90E2;
                --card-bg: #FFFFFF;
                --card-shadow: rgba(0, 0, 0, 0.1);
            }
            
            body {
                background-color: var(--background-color);
                font-family: 'Roboto', sans-serif;
                margin: 0;
                color: var(--text-color);
            }
            
            .quotes-container {
                background-color: var(--accent-color);
                color: white;
                padding: 12px 20px;
                text-align: center;
                font-style: italic;
                font-weight: 600;
                font-size: 1.15rem;
            }
            
            .quote-author {
                display: block;
                text-align: right;
                margin-top: 5px;
                font-size: 1rem;
                opacity: 0.85;
            }
            
            .header {
                background: var(--card-bg);
                padding: 10px 20px;
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
                cursor: pointer;
                transition: all 0.3s ease;
            }
            
            .nav-link:hover {
                font-family: 'Pacifico', cursive;
                color: var(--accent-color);
            }
            
            .card {
                background: var(--card-bg);
                max-width: 700px;
                margin: 40px auto;
                border-radius: 15px;
                box-shadow: 0 6px 20px var(--card-shadow);
                padding: 40px;
                transition: box-shadow 0.3s ease;
            }
            
            .card:hover {
                box-shadow: 0 8px 30px rgba(74, 144, 226, 0.5);
            }
            
            .card h1, .card h2 {
                color: var(--accent-color);
                margin-bottom: 20px;
            }
            
            .card p {
                font-size: 1.18rem;
                line-height: 1.7;
                margin: 15px 0;
            }
            
            .italic {
                font-style: italic;
                margin-top: 30px;
            }
            
            .picture {
                display: block;
                margin: 25px auto;
                width: 200px;
                height: 200px;
                border-radius: 50%;
                object-fit: cover;
                border: 4px solid var(--accent-color);
                box-shadow: 0 4px 10px var(--card-shadow);
            }
            
            .welcome-text {
                display: block;
                text-align: center;
                margin: 15px 0 35px;
                font-size: 1.8rem;
                font-weight: 600;
                color: var(--accent-color);
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
                margin: 20px auto;
                display: flex;
                gap: 40px;
                justify-content: center;
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
                list-style: none;
                padding: 0;
                font-size: 1.15rem;
            }
            
            .skills-list li {
                margin: 8px 0;
                padding-left: 1.5em;
                position: relative;
            }
            
            .skills-list li::before {
                content: '•';
                position: absolute;
                left: 0;
                color: var(--accent-color);
                font-weight: bold;
            }
            
            .contact-link {
                color: var(--accent-color);
                text-decoration: none;
                font-weight: 600;
                transition: color 0.3s ease;
            }
            
            .contact-link:hover {
                color: var(--text-color);
            }
            
            .rt-ListItem {
                margin: 8px 0;
            }
        """),
        
        # External fonts
        rx.el.link(
            rel="stylesheet",
            href="https://fonts.googleapis.com/css2?family=Pacifico&family=Roboto:wght@400;500;600&display=swap",
        ),
        
        # Components
        quote_banner(),
        navbar(),
        render_page(),
        
        # Animation intervals
        rx.interval(
            on_interval=State.type_welcome,
            interval=100,
            disabled=State.welcome_index >= 22,  # Length of welcome text
        ),
        
        max_width="1200px",
        padding="0",
        center_content=True,
    )


# ============= APP CONFIGURATION =============

app = rx.App(
    style={
        "font_family": "Roboto, sans-serif",
    }
)

app.add_page(
    index,
    route="/",
    title="Tole Caxtone Kirigha | Portfolio",
    description="Passionate developer specializing in web, mobile, AI, IoT, and robotics",
)

# For local development
if __name__ == "__main__":
    app.run()
