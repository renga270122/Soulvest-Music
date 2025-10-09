import streamlit as st
from utils.welcome import show_welcome_message
from pages.app_hits import load_app_hits, get_hit_stats

# 📊 App visit stats
hits = load_app_hits()
total_hits, daily_hits = get_hit_stats(hits)

# 📐 Mobile-friendly styling
st.markdown("""
    <style>
        .welcome-banner {
            font-size: 20px;
            line-height: 1.6;
            font-family: 'Segoe UI', sans-serif;
            text-align: center;
            padding: 1rem;
        }
        .welcome-date {
            font-size: 16px;
            color: #666;
        }
        .welcome-quote {
            font-size: 18px;
            font-style: italic;
            color: #444;
        }
        @media screen and (max-width: 600px) {
            .welcome-banner {
                font-size: 22px;
                padding: 0.5rem;
            }
            .welcome-date {
                font-size: 18px;
            }
            .welcome-quote {
                font-size: 20px;
            }
        }
    </style>
""", unsafe_allow_html=True)

def render_home():
    # 🌟 Modular welcome message (e.g., time-based greeting, quote)
    show_welcome_message()

    # 🏠 Main title
    st.title("🏠 Welcome to Soulvest Music")

    # 🎶 Intro message
    st.markdown("""
    Soulvest Music is your sanctuary for healing, empowerment, and soulful rituals.  
    Explore affirmations, chants, playlists, and personalized rituals to uplift your spirit.
    """)

    # 📈 App visit stats
    st.markdown(f"📈 **Total App Visits:** {total_hits}")
    st.markdown(f"📅 **Today's Visits:** {daily_hits}")

    # 🌅 Styled welcome banner
    st.markdown("""
        <div class="welcome-banner">
            <strong>Your sanctuary for healing music, affirmations, and spiritual growth</strong><br>
            <div class="welcome-date">🗓️ Thursday, 09 October 2025 — 05:12 PM</div>
            <div class="welcome-quote">💬 “The universe moves with you when you move with love.”</div>
        </div>
    """, unsafe_allow_html=True)

    # 🌈 Daily inspiration
    st.markdown("### 🌈 Daily Inspiration")
    st.info("“Let your inner music guide your outer journey.”")

    # 💖 Footer
    st.markdown("---")
    st.caption("Crafted with love and devotion 💖 by Soulvest.ai")
