"""
CRUD Operations Page
--------------------
Perform CRUD on player stats
Create, Read, Update, Delete operations using form-based UI
"""

import streamlit as st
import pandas as pd
from Services.crud_service import CRUDService


def show_page():
    st.title("🛠️ CRUD Operations")
    st.markdown("### Perform Create, Read, Update, Delete on Player Statistics")
    
    crud_service = CRUDService()
    
    # Create tabs for different operations
    tab1, tab2, tab3, tab4 = st.tabs(["➕ Create", "📖 Read", "✏️ Update", "🗑️ Delete"])
    
    with tab1:
        st.subheader("➕ Create New Player Record")
        st.markdown("*Add a new player to the database*")
        
        with st.form("create_player_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                player_name = st.text_input("Player Name *", placeholder="e.g., Virat Kohli")
                country = st.text_input("Country *", placeholder="e.g., India")
                playing_role = st.selectbox(
                    "Playing Role *",
                    ["Batsman", "Bowler", "All-rounder", "Wicket-keeper"]
                )
                batting_style = st.selectbox(
                    "Batting Style *",
                    ["Right-hand bat", "Left-hand bat", "N/A"]
                )
            
            with col2:
                bowling_style = st.selectbox(
                    "Bowling Style *",
                    ["Right-arm fast", "Right-arm medium", "Right-arm spin", 
                     "Left-arm fast", "Left-arm medium", "Left-arm spin", "N/A"]
                )
                date_of_birth = st.date_input("Date of Birth")
                jersey_number = st.number_input("Jersey Number", min_value=0, max_value=999, value=0)
                is_active = st.checkbox("Active Player", value=True)
            
            submit_create = st.form_submit_button("➕ Add Player", type="primary", use_container_width=True)
            
            if submit_create:
                if player_name and country:
                    try:
                        player_data = {
                            'player_name': player_name,
                            'country': country,
                            'playing_role': playing_role,
                            'batting_style': batting_style,
                            'bowling_style': bowling_style,
                            'date_of_birth': date_of_birth,
                            'jersey_number': jersey_number if jersey_number > 0 else None,
                            'is_active': is_active
                        }
                        
                        result = crud_service.create_player(player_data)
                        st.success(f"✅ Player '{player_name}' added successfully!")
                        st.balloons()
                    except Exception as e:
                        st.error(f"❌ Error creating player: {str(e)}")
                else:
                    st.warning("⚠️ Please fill in all required fields marked with *")
    
    with tab2:
        st.subheader("📖 Read Player Records")
        st.markdown("*View and search player information*")
        
        # Search filters
        col1, col2, col3 = st.columns(3)
        with col1:
            search_name = st.text_input("🔍 Search by Name", placeholder="Enter player name")
        with col2:
            filter_country = st.selectbox("Filter by Country", ["All", "India", "Australia", "England", "Pakistan", "Others"])
        with col3:
            filter_role = st.selectbox("Filter by Role", ["All", "Batsman", "Bowler", "All-rounder", "Wicket-keeper"])
        
        if st.button("🔍 Search Players", type="primary"):
            try:
                filters = {}
                if search_name:
                    filters['player_name'] = search_name
                if filter_country != "All":
                    filters['country'] = filter_country
                if filter_role != "All":
                    filters['playing_role'] = filter_role
                
                with st.spinner("Fetching player data..."):
                    players = crud_service.read_players(filters)
                
                if players and len(players) > 0:
                    df = pd.DataFrame(players)
                    st.success(f"✅ Found {len(df)} player(s)")
                    st.dataframe(
                        df,
                        use_container_width=True,
                        hide_index=True,
                        column_config={
                            "player_id": st.column_config.NumberColumn("ID", width="small"),
                            "player_name": st.column_config.TextColumn("Name", width="medium"),
                            "country": st.column_config.TextColumn("Country", width="small"),
                            "playing_role": st.column_config.TextColumn("Role", width="medium"),
                            "is_active": st.column_config.CheckboxColumn("Active"),
                        }
                    )
                    
                    # Download option
                    csv = df.to_csv(index=False)
                    st.download_button(
                        label="📥 Download as CSV",
                        data=csv,
                        file_name="players.csv",
                        mime="text/csv"
                    )
                else:
                    st.info("📭 No players found matching the criteria.")
            except Exception as e:
                st.error(f"❌ Error fetching players: {str(e)}")
    
    with tab3:
        st.subheader("✏️ Update Player Record")
        st.markdown("*Modify existing player information*")
        
        # First select player to update
        try:
            all_players = crud_service.read_players()
            if all_players and len(all_players) > 0:
                player_names = [p['player_name'] for p in all_players]
                selected_player = st.selectbox("Select Player to Update", player_names)
                
                if selected_player:
                    # Get player details
                    player_data = next((p for p in all_players if p['player_name'] == selected_player), None)
                    
                    if player_data:
                        with st.form("update_player_form"):
                            st.info(f"Updating: **{selected_player}**")
                            
                            col1, col2 = st.columns(2)
                            
                            with col1:
                                new_country = st.text_input("Country", value=player_data.get('country', ''))
                                new_role = st.selectbox(
                                    "Playing Role",
                                    ["Batsman", "Bowler", "All-rounder", "Wicket-keeper"],
                                    index=["Batsman", "Bowler", "All-rounder", "Wicket-keeper"].index(player_data.get('playing_role', 'Batsman'))
                                )
                                new_batting_style = st.text_input("Batting Style", value=player_data.get('batting_style', ''))
                            
                            with col2:
                                new_bowling_style = st.text_input("Bowling Style", value=player_data.get('bowling_style', ''))
                                new_jersey = st.number_input("Jersey Number", min_value=0, max_value=999, 
                                                            value=int(player_data.get('jersey_number', 0)))
                                new_active = st.checkbox("Active Player", value=bool(player_data.get('is_active', True)))
                            
                            submit_update = st.form_submit_button("✏️ Update Player", type="primary", use_container_width=True)
                            
                            if submit_update:
                                try:
                                    update_data = {
                                        'player_id': player_data['player_id'],
                                        'country': new_country,
                                        'playing_role': new_role,
                                        'batting_style': new_batting_style,
                                        'bowling_style': new_bowling_style,
                                        'jersey_number': new_jersey if new_jersey > 0 else None,
                                        'is_active': new_active
                                    }
                                    
                                    result = crud_service.update_player(update_data)
                                    st.success(f"✅ Player '{selected_player}' updated successfully!")
                                except Exception as e:
                                    st.error(f"❌ Error updating player: {str(e)}")
            else:
                st.info("📭 No players available in the database.")
        except Exception as e:
            st.error(f"❌ Error loading players: {str(e)}")
    
    with tab4:
        st.subheader("🗑️ Delete Player Record")
        st.markdown("*Remove a player from the database*")
        
        st.warning("⚠️ **Warning**: Deleting a player will permanently remove their record from the database!")
        
        try:
            all_players = crud_service.read_players()
            if all_players and len(all_players) > 0:
                player_names = [p['player_name'] for p in all_players]
                selected_player = st.selectbox("Select Player to Delete", player_names, key="delete_select")
                
                if selected_player:
                    player_data = next((p for p in all_players if p['player_name'] == selected_player), None)
                    
                    if player_data:
                        st.info(f"**Player Details:**")
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.write(f"**Name:** {player_data.get('player_name')}")
                        with col2:
                            st.write(f"**Country:** {player_data.get('country')}")
                        with col3:
                            st.write(f"**Role:** {player_data.get('playing_role')}")
                        
                        st.divider()
                        
                        # Confirmation
                        confirm = st.checkbox(f"I confirm I want to delete **{selected_player}**")
                        
                        if st.button("🗑️ Delete Player", type="primary", disabled=not confirm, use_container_width=True):
                            try:
                                result = crud_service.delete_player(player_data['player_id'])
                                st.success(f"✅ Player '{selected_player}' deleted successfully!")
                                st.rerun()
                            except Exception as e:
                                st.error(f"❌ Error deleting player: {str(e)}")
            else:
                st.info("📭 No players available in the database.")
        except Exception as e:
            st.error(f"❌ Error loading players: {str(e)}")
