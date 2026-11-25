"""
SQL Queries Page (FIXED VERSION)
----------------
SQL query interface and analytics with CORRECTED queries for your database schema
"""

import streamlit as st
import pandas as pd
from Database.Repository import Repository


def show_page():
    st.title("📊 SQL Query Interface & Analytics")
    st.markdown("### Run Custom SQL Queries and Practice Analytics")
    
    # Check database connection status
    try:
        repo = Repository()
        # Test connection
        test_result = repo.execute_query("SELECT 1 as test")
        if test_result:
            st.success("✅ Database connected successfully!")
        else:
            st.error("⚠️ Database connection failed!")
            return
    except Exception as e:
        st.error(f"❌ Database not available: {str(e)}")
        return
    
    # Custom Query Section Only
    st.subheader("✍️ Custom SQL Query Editor")
    st.markdown("*Write and execute your own SQL queries*")
    
    st.info("💡 **Tip**: You can write any SELECT query to explore the database.")
    
    # Example queries in an expander
    with st.expander("📚 Example Queries", expanded=False):
        st.markdown("""
        **Q1: All Indian Players**
        ```sql
        SELECT p.full_name, p.role, p.batting_style, t.team_name
        FROM players p
        JOIN teams t ON p.team_id = t.team_id
        WHERE t.team_name = 'India'
        ORDER BY p.full_name;
        ```
        
        **Q2: Top 10 ODI Run Scorers**
        ```sql
        SELECT p.full_name, t.team_name, ps.runs, ps.batting_average, ps.hundreds
        FROM player_statistics ps
        JOIN players p ON ps.player_id = p.player_id
        JOIN teams t ON p.team_id = t.team_id
        WHERE ps.format = 'ODI'
        ORDER BY ps.runs DESC
        LIMIT 10;
        ```
        
        **Q3: All Venues**
        ```sql
        SELECT venue_name, city, country, capacity
        FROM venues
        ORDER BY capacity DESC;
        ```
        
        **Q4: Recent Matches**
        ```sql
        SELECT m.match_id, t1.team_name as team1, t2.team_name as team2,
               v.venue_name, v.city, m.match_date, m.status
        FROM matches m
        JOIN teams t1 ON m.team1_id = t1.team_id
        JOIN teams t2 ON m.team2_id = t2.team_id
        JOIN venues v ON m.venue_id = v.venue_id
        ORDER BY m.match_date DESC
        LIMIT 20;
        ```
        
        **Q5: Players by Role**
        ```sql
        SELECT role, COUNT(*) as player_count
        FROM players
        GROUP BY role
        ORDER BY player_count DESC;
        ```
        
        **Q6: Database Summary**
        ```sql
        SELECT 
            (SELECT COUNT(*) FROM players) as total_players,
            (SELECT COUNT(*) FROM teams) as total_teams,
            (SELECT COUNT(*) FROM venues) as total_venues,
            (SELECT COUNT(*) FROM matches) as total_matches,
            (SELECT COUNT(*) FROM player_statistics) as total_stats;
        ```
        """)
    
    custom_query = st.text_area(
        "Enter your SQL query:",
        height=200,
        placeholder="SELECT * FROM players LIMIT 10;",
        help="Only SELECT queries are allowed for security."
    )
    
    col1, col2, col3 = st.columns([1, 1, 4])
    with col1:
        execute_btn = st.button("▶️ Execute Query", type="primary", use_container_width=True)
    with col2:
        clear_btn = st.button("🗑️ Clear", use_container_width=True)
    with col3:
        st.caption("*Only SELECT statements are permitted*")
    
    if clear_btn:
        st.rerun()
    
    if execute_btn and custom_query.strip():
        # Security check - only allow SELECT statements
        if custom_query.strip().upper().startswith('SELECT'):
            try:
                with st.spinner("Executing query..."):
                    results = repo.execute_query(custom_query)
                
                if results:
                    df = pd.DataFrame(results)
                    st.success(f"✅ Query executed successfully! ({len(df)} rows returned)")
                    
                    # Display results
                    st.dataframe(df, use_container_width=True, hide_index=True)
                    
                    # Download option
                    csv = df.to_csv(index=False)
                    st.download_button(
                        label="📥 Download Results as CSV",
                        data=csv,
                        file_name="query_results.csv",
                        mime="text/csv"
                    )
                    
                    # Show row count
                    st.info(f"📊 Total rows: {len(df)} | Columns: {len(df.columns)}")
                else:
                    st.warning("⚠️ Query executed but returned no results.")
            
            except Exception as e:
                st.error(f"❌ Query execution failed: {str(e)}")
                with st.expander("🔍 Error Details"):
                    st.code(str(e))
        else:
            st.error("⚠️ Only SELECT queries are allowed for security reasons.")


def display_query_section(queries_dict, repo):
    """Helper function - no longer used"""
    pass
