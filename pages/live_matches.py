"""
Live Matches Page
-----------------
Displays live match data from Cricbuzz API
"""

import streamlit as st
from Services.match_service import MatchService
import pandas as pd


def show_page():
    st.title("🏏 Live Matches")
    st.markdown("### Current Live Cricket Matches")
    
    # Refresh button
    col1, col2 = st.columns([6, 1])
    with col2:
        refresh = st.button("🔄 Refresh", use_container_width=True)
    
    try:
        match_service = MatchService()
        
        with st.spinner("Fetching live match data from Cricbuzz API..."):
            response = match_service.get_live_matches()
        
        # Debug: Show raw response structure
        if st.checkbox("🔍 Show API Response (Debug)", value=False):
            st.json(response)
        
        # Handle different response formats
        matches = []
        if isinstance(response, dict):
            # Check common response structures
            if 'typeMatches' in response:
                # Cricbuzz API v1 format
                for type_match in response.get('typeMatches', []):
                    for series_match in type_match.get('seriesMatches', []):
                        if 'seriesAdWrapper' in series_match:
                            matches.extend(series_match['seriesAdWrapper'].get('matches', []))
            elif 'matches' in response:
                matches = response['matches']
            elif 'data' in response:
                matches = response['data']
        elif isinstance(response, list):
            matches = response
        
        if matches and len(matches) > 0:
            st.success(f"✅ Found {len(matches)} live match(es)")
            
            for idx, match in enumerate(matches, 1):
                # Extract match info (handle different formats)
                match_info = match.get('matchInfo', match)
                
                with st.expander(
                    f"🏏 Match {idx}: {match_info.get('seriesName', match_info.get('series', 'Unknown Series'))}", 
                    expanded=(idx == 1)
                ):
                    # Match details in columns
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.write(f"**🏆 Series:** {match_info.get('seriesName', match_info.get('series', 'N/A'))}")
                        st.write(f"**🏟️ Venue:** {match_info.get('venueInfo', {}).get('ground', match_info.get('venue', 'N/A'))}")
                        st.write(f"**📍 City:** {match_info.get('venueInfo', {}).get('city', match_info.get('city', 'N/A'))}")
                    
                    with col2:
                        st.write(f"**⚡ Status:** {match_info.get('status', match_info.get('matchState', 'N/A'))}")
                        st.write(f"**🏏 Match Type:** {match_info.get('matchFormat', match_info.get('match_type', 'N/A'))}")
                        st.write(f"**📅 Date:** {match_info.get('matchStartTimestamp', match_info.get('date', 'N/A'))}")
                    
                    st.divider()
                    
                    # Teams
                    team1 = match_info.get('team1', {}).get('teamName', match_info.get('team1', 'Team 1'))
                    team2 = match_info.get('team2', {}).get('teamName', match_info.get('team2', 'Team 2'))
                    
                    st.write("**👥 Teams:**")
                    st.info(f"{team1} vs {team2}")
                    
                    # Match score
                    match_score = match.get('matchScore', {})
                    if match_score:
                        st.write("**📊 Score:**")
                        team1_score = match_score.get('team1Score', {})
                        team2_score = match_score.get('team2Score', {})
                        
                        if team1_score:
                            st.write(f"{team1}: {team1_score.get('inngs1', {}).get('runs', 0)}/{team1_score.get('inngs1', {}).get('wickets', 0)}")
                        if team2_score:
                            st.write(f"{team2}: {team2_score.get('inngs1', {}).get('runs', 0)}/{team2_score.get('inngs1', {}).get('wickets', 0)}")
                    
                    # Match description/status
                    if match_info.get('stateTitle'):
                        st.info(match_info['stateTitle'])
        else:
            st.info("⏳ No live matches at the moment. Check back later!")
            st.markdown("""
            **Note:** Live matches data is fetched from Cricbuzz API. 
            Matches will appear here when cricket matches are in progress.
            
            **Possible reasons:**
            - No cricket matches currently live
            - API endpoint requires different parameters
            - API subscription may need updating
            """)
    
    except Exception as e:
        st.error(f"❌ Error fetching live matches: {str(e)}")
        
        with st.expander("🔍 Troubleshooting"):
            st.markdown(f"""
            **Error Details:** `{type(e).__name__}: {str(e)}`
            
            **Common Issues:**
            1. **API key not configured properly**
               - Check `.env` file has valid RAPIDAPI_KEY
            
            2. **API rate limit exceeded**
               - Free tier: 10 requests/minute
               - Wait a minute and try again
            
            3. **Network connectivity issues**
               - Check internet connection
            
            4. **Invalid API endpoint**
               - API structure may have changed
               - Check RapidAPI documentation
            
            **Current Configuration:**
            - API Host: {st.session_state.get('api_host', 'Not loaded')}
            - API Key: {'✅ Configured' if st.secrets.get('RAPIDAPI_KEY') or True else '❌ Missing'}
            
            **Solution:**
            - Verify your RapidAPI key in `.env` file
            - Ensure API subscription is active at RapidAPI.com
            - Try the debug checkbox above to see raw API response
            """)
            
            st.code(f"Exception Type: {type(e).__name__}\nException Message: {str(e)}", language="python")
