import streamlit as st
from typing import Dict
import pandas as pd
from datetime import datetime

# Translations dictionary
TRANSLATIONS = {
    "en": {
        "nav_home": "Home",
        "nav_companies": "Companies",
        "nav_reviews": "Reviews",
        "nav_admin": "Admin Login",
        "hero_title": "Find Your Perfect Internship",
        "hero_subtitle": "Read real experiences from former interns and make informed decisions about your future internship.",
        "filter_title": "Quick Search",
        "filter_company": "Company Name",
        "filter_department": "Department",
        "filter_rating": "Minimum Rating",
        "popular_reviews": "Popular Reviews",
        "search_button": "Search",
    },
    "tr": {
        "nav_home": "Ana Sayfa",
        "nav_companies": "Şirketler",
        "nav_reviews": "Değerlendirmeler",
        "nav_admin": "Admin Girişi",
        "hero_title": "Hayalindeki Stajı Bul",
        "hero_subtitle": "Eski stajyerlerin gerçek deneyimlerini oku ve gelecekteki stajın hakkında bilinçli kararlar al.",
        "filter_title": "Hızlı Arama",
        "filter_company": "Şirket Adı",
        "filter_department": "Departman",
        "filter_rating": "Minimum Puan",
        "popular_reviews": "Popüler Değerlendirmeler",
        "search_button": "Ara",
    }
}

def init_session_state():
    """Initialize session state variables"""
    if 'language' not in st.session_state:
        st.session_state.language = 'tr'

def get_text(key: str) -> str:
    """Get translated text based on current language"""
    return TRANSLATIONS[st.session_state.language][key]

def apply_custom_css():
    """Apply custom CSS styles"""
    st.markdown("""
        <style>
        .stApp {
            max-width: 1200px;
            margin: 0 auto;
        }
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 0;
            margin-bottom: 2rem;
        }
        .hero-section {
            text-align: center;
            padding: 4rem 2rem;
            background-color: #f8f9fa;
            border-radius: 10px;
            margin-bottom: 2rem;
        }
        .filter-section {
            background-color: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .popular-reviews {
            margin-top: 2rem;
        }
        .review-card {
            padding: 1rem;
            border: 1px solid #eee;
            border-radius: 5px;
            margin-bottom: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)

def render_navbar():
    """Render navigation bar"""
    col1, col2, col3, col4, col5, col6 = st.columns([2, 1, 1, 1, 1, 1])
    
    with col1:
        # Kompakt logo için
        st.image("assets/intern-insider-compact-logo.svg", width=100)
    
    with col2:
        st.button(get_text("nav_home"))
    
    with col3:
        st.button(get_text("nav_companies"))
    
    with col4:
        st.button(get_text("nav_reviews"))
    
    with col5:
        # Language toggle
        if st.button("🌐 TR/EN"):
            st.session_state.language = 'en' if st.session_state.language == 'tr' else 'tr'
            st.experimental_rerun()
    
    with col6:
        if st.button(get_text("nav_admin")):
            st.session_state.page = "admin_login"
            st.experimental_rerun()

def render_logo():
    """Render the logo at the top of the app"""
    st.image("assets/intern-insider-logo.png")

def render_hero_section():
    """Render hero section"""
    st.markdown(f"""
        <div class="hero-section" style="background-color: #f0f4f8;">
            <h1 style="color: #ff8c00;">{get_text('hero_title')}</h1>  <!-- Soft turuncu -->
            <p style="color: #005f73;">{get_text('hero_subtitle')}</p>  <!-- Lacivert ile uyumlu soft mavi -->
        </div>
    """, unsafe_allow_html=True)


def render_quick_filter():
    """Render quick filter section"""
    st.markdown(f"### {get_text('filter_title')}")
    
    with st.form("quick_filter"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            company = st.text_input(get_text("filter_company"))
        
        with col2:
            departments = ["Computer Engineering", "Industrial Engineering", "Mechanical Engineering"]
            department = st.selectbox(get_text("filter_department"), departments)
        
        with col3:
            rating = st.slider(get_text("filter_rating"), 1, 5, 3)
        
        submitted = st.form_submit_button(get_text("search_button"))
        if submitted:
            # Handle filter submission
            pass

def render_popular_reviews():
    """Render popular reviews section"""
    st.markdown(f"### {get_text('popular_reviews')}")
    
    # Sample reviews data - In production, Database'den çekilecek
    sample_reviews = [
        {
            "company": "Tech Corp",
            "rating": 4.5,
            "department": "Computer Engineering",
            "review": "Great learning experience with modern technologies...",
            "date": "2024-03-15"
        },
        {
            "company": "Industry Ltd",
            "rating": 4.8,
            "department": "Industrial Engineering",
            "review": "Excellent mentorship program and hands-on projects...",
            "date": "2024-03-10"
        }
    ]
    
    for review in sample_reviews:
        with st.container():
            st.markdown(f"""
                <div class="review-card">
                    <h4>{review['company']} - ⭐ {review['rating']}</h4>
                    <p><em>{review['department']}</em></p>
                    <p>{review['review']}</p>
                    <small>{review['date']}</small>
                </div>
            """, unsafe_allow_html=True)

def main():
    """Main function to render the homepage"""
    st.set_page_config(
        page_title="Intern Insider",
        page_icon="👩‍💻",
        layout="wide"
    )
    
    init_session_state()
    
    apply_custom_css()

    render_logo()
    render_navbar()
    render_hero_section()
    render_quick_filter()
    render_popular_reviews()


if __name__ == "__main__":
    main()