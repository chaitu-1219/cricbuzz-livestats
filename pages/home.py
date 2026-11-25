"""
Home Page
---------
Overview and About the Project page
"""

import streamlit as st


def show_page():
    st.title("🏏 Cricbuzz LiveStats")
    st.subheader("Real-Time Cricket Insights & SQL-Based Analytics")
    
    st.markdown("""
    ## Welcome to Cricbuzz LiveStats
    
    This comprehensive cricket analytics dashboard integrates live data from the Cricbuzz API 
    with a SQL database to create an interactive web application.
    
    ### 🎯 Features:
    - **⚡ Live Matches**: View real-time match updates and detailed scorecards
    - **📊 Top Stats**: Analyze top batting and bowling statistics
    - **📈 SQL Analytics**: Run custom SQL queries for advanced analytics
    - **🛠️ CRUD Operations**: Manage player statistics in the database
    
    ### 💼 Business Use Cases:
    1. **📺 Sports Media & Broadcasting** - Real-time updates for commentary teams
    2. **🎮 Fantasy Cricket Platforms** - Player form analysis and performance tracking
    3. **📈 Cricket Analytics Firms** - Advanced statistical modeling
    4. **🎓 Educational Institutions** - Teaching database operations with real data
    5. **🎲 Sports Betting & Prediction** - Historical performance analysis
    
    ### 🛠️ Tech Stack:
    - **Frontend**: Streamlit
    - **API**: RapidAPI Cricbuzz API
    - **Database**: MySQL (Database-agnostic design)
    - **Data Processing**: Pandas, NumPy
    - **Visualization**: Plotly, Matplotlib
    
    ### 📋 Project Structure:
    ```
    cricbuzz_livestats/
    ├── app.py                    # Main entry point
    ├── requirements.txt          # Python packages
    ├── README.md                 # Project documentation
    ├── pages/                    # Streamlit pages
    │   ├── home.py
    │   ├── live_matches.py
    │   ├── top_stats.py
    │   ├── sql_queries.py
    │   └── crud_operations.py
    ├── utils/                    # Utility files
    │   └── db_connection.py      # Database connection logic
    └── notebooks/                # Practice Jupyter notebooks
        └── data_fetching.ipynb   # API testing and data push
    ```
    
    ### 🚀 Getting Started:
    1. Configure your API credentials in Settings
    2. Set up database connection
    3. Navigate through pages using the sidebar menu
    
    ### 📚 Skills Demonstrated:
    `Python` • `SQL` • `Streamlit` • `JSON` • `REST API` • `Database Management` • `Data Analytics`
    
    ---
    
    💡 **Tip**: Use the sidebar menu to navigate through different sections of the application!
    """)
    
    # Quick stats or info boxes
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Pages", "5", help="Interactive pages in the dashboard")
    
    with col2:
        st.metric("SQL Queries", "25+", help="Practice SQL questions included")
    
    with col3:
        st.metric("API Integration", "✓", help="Cricbuzz API connected")
    
    with col4:
        st.metric("Database", "MySQL", help="SQL database support")
