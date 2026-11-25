"""
Top Stats Page
--------------
Shows top batting/bowling stats
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from Services.analytics_service import AnalyticsService


def show_page():
    st.title("📊 Top Player Statistics")
    st.markdown("### View Top Batting and Bowling Performance")
    
    analytics_service = AnalyticsService()
    
    # Add filters
    col1, col2 = st.columns([3, 1])
    with col1:
        format_filter = st.selectbox(
            "Cricket Format",
            ["All Formats", "Test", "ODI", "T20I"],
            help="Filter statistics by cricket format"
        )
    with col2:
        limit = st.number_input("Top N Players", min_value=5, max_value=50, value=10, step=5)
    
    tab1, tab2 = st.tabs(["🏏 Batting Stats", "⚾ Bowling Stats"])
    
    with tab1:
        st.subheader("🏏 Top Batsmen")
        st.markdown("*Highest run scorers with best batting averages*")
        
        try:
            with st.spinner("Loading batting statistics..."):
                batting_stats = analytics_service.get_top_batsmen(limit=limit, format=format_filter)
            
            if batting_stats and len(batting_stats) > 0:
                df = pd.DataFrame(batting_stats)
                
                # Display dataframe
                st.dataframe(
                    df,
                    use_container_width=True,
                    hide_index=True,
                    column_config={
                        "player_name": st.column_config.TextColumn("Player Name", width="medium"),
                        "team_name": st.column_config.TextColumn("Team", width="small"),
                        "runs": st.column_config.NumberColumn("Total Runs", format="%d"),
                        "batting_avg": st.column_config.NumberColumn("Average", format="%.2f"),
                        "matches": st.column_config.NumberColumn("Matches", format="%d"),
                        "centuries": st.column_config.NumberColumn("100s", format="%d"),
                        "half_centuries": st.column_config.NumberColumn("50s", format="%d"),
                        "strike_rate": st.column_config.NumberColumn("Strike Rate", format="%.2f"),
                    }
                )
                
                # Visualization
                st.markdown("#### 📈 Runs Distribution")
                fig = px.bar(
                    df,
                    x='player_name',
                    y='runs',
                    title='Top Run Scorers',
                    labels={'player_name': 'Player', 'runs': 'Total Runs'},
                    color='runs',
                    color_continuous_scale='Blues'
                )
                fig.update_layout(xaxis_tickangle=-45)
                st.plotly_chart(fig, use_container_width=True)
                
                # Additional stats
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Highest Scorer", df.iloc[0]['player_name'], f"{df.iloc[0]['runs']} runs")
                with col2:
                    st.metric("Best Average", df.loc[df['batting_avg'].idxmax()]['player_name'], 
                             f"{df['batting_avg'].max():.2f}")
                with col3:
                    st.metric("Total Centuries", int(df['centuries'].sum()))
                
            else:
                st.info("📭 No batting statistics available.")
                st.markdown("*Data might not be loaded into the database yet.*")
        
        except Exception as e:
            st.error(f"❌ Error loading batting stats: {str(e)}")
            st.info("💡 Ensure database is connected and data is populated.")
    
    with tab2:
        st.subheader("⚾ Top Bowlers")
        st.markdown("*Most successful wicket-takers with best bowling averages*")
        
        try:
            with st.spinner("Loading bowling statistics..."):
                bowling_stats = analytics_service.get_top_bowlers(limit=limit, format=format_filter)
            
            if bowling_stats and len(bowling_stats) > 0:
                df = pd.DataFrame(bowling_stats)
                
                # Display dataframe
                st.dataframe(
                    df,
                    use_container_width=True,
                    hide_index=True,
                    column_config={
                        "player_name": st.column_config.TextColumn("Player Name", width="medium"),
                        "team_name": st.column_config.TextColumn("Team", width="small"),
                        "wickets": st.column_config.NumberColumn("Total Wickets", format="%d"),
                        "bowling_avg": st.column_config.NumberColumn("Average", format="%.2f"),
                        "economy_rate": st.column_config.NumberColumn("Economy", format="%.2f"),
                        "matches": st.column_config.NumberColumn("Matches", format="%d"),
                    }
                )
                
                # Visualization
                st.markdown("#### 📈 Wickets Distribution")
                fig = px.bar(
                    df,
                    x='player_name',
                    y='wickets',
                    title='Top Wicket Takers',
                    labels={'player_name': 'Player', 'wickets': 'Total Wickets'},
                    color='wickets',
                    color_continuous_scale='Reds'
                )
                fig.update_layout(xaxis_tickangle=-45)
                st.plotly_chart(fig, use_container_width=True)
                
                # Additional stats
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Top Wicket Taker", df.iloc[0]['player_name'], 
                             f"{int(df.iloc[0]['wickets'])} wickets")
                with col2:
                    st.metric("Best Average", df.loc[df['bowling_avg'].idxmin()]['player_name'], 
                             f"{df['bowling_avg'].min():.2f}")
                with col3:
                    st.metric("Best Economy", df.loc[df['economy_rate'].idxmin()]['player_name'],
                             f"{df['economy_rate'].min():.2f}")
                
            else:
                st.info("📭 No bowling statistics available.")
                st.markdown("*Data might not be loaded into the database yet.*")
        
        except Exception as e:
            st.error(f"❌ Error loading bowling stats: {str(e)}")
            st.info("💡 Ensure database is connected and data is populated.")
