"""
Main Entry Point
----------------
Starts the Streamlit application for Cricbuzz LiveStats.

This is the main entry point for the Streamlit app.
Navigate through different pages using the sidebar menu.
"""

import streamlit as st
from streamlit_option_menu import option_menu

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title=" Cricbuzz LiveStats",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/yourusername/cricbuzz-livestats',
        'Report a bug': 'https://github.com/yourusername/cricbuzz-livestats/issues',
        'About': """
        # Cricbuzz LiveStats
        Real-Time Cricket Insights & SQL-Based Analytics
        
        **Version:** 1.0.0
        **Tech Stack:** Python • SQL • Streamlit • REST API
        """
    }
)

# -----------------------------
# Sidebar Navigation
# -----------------------------

with st.sidebar:
    # Add custom CSS for better visibility in both dark and light mode
    st.markdown("""
        <style>
        /* ── Nav link: unselected ── */
        [data-testid="stSidebar"] nav a,
        [data-testid="stSidebar"] .nav-link {
            color: var(--text-color) !important;
            background-color: transparent !important;
        }

        /* ── Nav link: hover ── */
        [data-testid="stSidebar"] nav a:hover,
        [data-testid="stSidebar"] .nav-link:hover {
            background-color: rgba(255, 107, 53, 0.15) !important;
            color: var(--text-color) !important;
        }

        /* ── Nav link: selected ── */
        [data-testid="stSidebar"] .nav-link-selected,
        [data-testid="stSidebar"] nav a[aria-selected="true"] {
            background-color: #ff6b35 !important;
            color: #ffffff !important;
            font-weight: bold !important;
        }

        /* ── Icons: always orange except when selected ── */
        [data-testid="stSidebar"] .nav-link i,
        [data-testid="stSidebar"] .nav-link svg {
            color: #ff6b35 !important;
        }

        /* ── Icons on selected item: white ── */
        [data-testid="stSidebar"] .nav-link-selected i,
        [data-testid="stSidebar"] .nav-link-selected svg {
            color: #ffffff !important;
        }

        /* ── Sidebar title ── */
        [data-testid="stSidebar"] h2 {
            color: var(--text-color) !important;
        }

        /* ── About expander text ── */
        [data-testid="stSidebar"] .streamlit-expanderContent p,
        [data-testid="stSidebar"] .streamlit-expanderContent li,
        [data-testid="stSidebar"] .streamlit-expanderContent strong {
            color: var(--text-color) !important;
        }

        /* ── Footer text ── */
        [data-testid="stSidebar"] .sidebar-footer p {
            color: var(--text-color) !important;
            opacity: 0.6;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center;'>🏏 Cricbuzz LiveStats</h2>", unsafe_allow_html=True)
    
    selected = option_menu(
        menu_title=None,  # Remove duplicate title
        options=[
            "Home",
            "Live Matches",
            "Top Stats",
            "SQL Queries",
            "CRUD Operations",
        ],
        icons=[
            "house-fill",
            "broadcast",
            "trophy-fill",
            "code-square",
            "database-fill-gear",
        ],
        default_index=0,
        styles={
            "container": {
                "padding": "0!important",
                "background-color": "transparent",
            },
            "icon": {
                "color": "#ff6b35",
                "font-size": "18px",
            },
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "0px",
                "padding": "10px 15px",
                "background-color": "transparent",
                "--hover-color": "rgba(255,107,53,0.12)",
            },
            "nav-link-selected": {
                "background-color": "#ff6b35",
                "color": "#ffffff",
                "font-weight": "bold",
            },
        }
    )
    
    st.divider()
    
    # Sidebar info with better visibility
    with st.expander("ℹ️ About", expanded=False):
        st.markdown("""
        **Cricbuzz LiveStats** provides:
        - ⚡ Real-time match updates
        - 📊 Player statistics
        - 📈 SQL-driven analytics
        - 🛠️ CRUD operations

        Built with Python, Streamlit, and MySQL.
        """)
    
    # Footer
    st.markdown("---")
    st.markdown("<p style='text-align: center; opacity: 0.6;'>🏏 Cricbuzz LiveStats v1.0</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; opacity: 0.6;'>© 2026 | Sports Analytics</p>", unsafe_allow_html=True)

# -----------------------------
# Page Navigation
# -----------------------------

if selected == "Home":
    from pages.home import show_page
    show_page()

elif selected == "Live Matches":
    from pages.live_matches import show_page
    show_page()

elif selected == "Top Stats":
    from pages.top_stats import show_page
    show_page()

elif selected == "SQL Queries":
    from pages.sql_queries import show_page
    show_page()

elif selected == "CRUD Operations":
    from pages.crud_operations import show_page
    show_page()

# -----------------------------
# Hide Streamlit Branding (Optional)
# -----------------------------

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Hide the default page navigation */
    [data-testid="stSidebarNav"] {
        display: none;
    }
    
    /* Hide app text at top of sidebar */
    section[data-testid="stSidebar"] > div:first-child {
        padding-top: 0rem;
    }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)