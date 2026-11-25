"""
api/players.py

Player-related API wrapper for Cricbuzz RapidAPI.

Author: Your Name
Project: Cricbuzz LiveStats

Features
--------
✓ Player Information
✓ Player Statistics
✓ Career Statistics
✓ Batting Statistics
✓ Bowling Statistics
✓ Search Helper
✓ Logging
✓ Error Handling
✓ Type Hints
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional

from Api.client import client

logger = logging.getLogger(__name__)


class PlayersAPI:
    """
    Wrapper class for all player endpoints.
    """

    # --------------------------------------------------
    # Endpoint Constants
    # --------------------------------------------------

    PLAYER_INFO = "players/get-info"

    PLAYER_STATS = "players/get-stats"

    PLAYER_CAREER = "players/get-career"

    PLAYER_BATTING = "players/get-batting"

    PLAYER_BOWLING = "players/get-bowling"

    # --------------------------------------------------

    def get_player_info(
        self,
        player_id: int,
    ) -> Dict[str, Any]:
        """
        Get complete player profile.
        """

        logger.info("Fetching player info : %s", player_id)

        return client.get(
            self.PLAYER_INFO,
            params={
                "playerId": player_id
            },
        )

    # --------------------------------------------------

    def get_player_stats(
        self,
        player_id: int,
    ) -> Dict[str, Any]:
        """
        Get overall player statistics.
        """

        logger.info("Fetching player statistics : %s", player_id)

        return client.get(
            self.PLAYER_STATS,
            params={
                "playerId": player_id
            },
        )

    # --------------------------------------------------

    def get_player_career(
        self,
        player_id: int,
    ) -> Dict[str, Any]:
        """
        Fetch complete career statistics.
        """

        logger.info("Fetching player career : %s", player_id)

        return client.get(
            self.PLAYER_CAREER,
            params={
                "playerId": player_id
            },
        )

    # --------------------------------------------------

    def get_batting_stats(
        self,
        player_id: int,
    ) -> Dict[str, Any]:
        """
        Batting statistics.
        """

        logger.info("Fetching batting stats : %s", player_id)

        return client.get(
            self.PLAYER_BATTING,
            params={
                "playerId": player_id
            },
        )

    # --------------------------------------------------

    def get_bowling_stats(
        self,
        player_id: int,
    ) -> Dict[str, Any]:
        """
        Bowling statistics.
        """

        logger.info("Fetching bowling stats : %s", player_id)

        return client.get(
            self.PLAYER_BOWLING,
            params={
                "playerId": player_id
            },
        )

    # --------------------------------------------------
    # Helper Methods
    # --------------------------------------------------

    def get_player_name(
        self,
        player_id: int,
    ) -> Optional[str]:
        """
        Return player name.
        """

        data = self.get_player_info(player_id)

        return (
            data.get("name")
            or data.get("playerName")
            or data.get("fullName")
        )

    # --------------------------------------------------

    def get_country(
        self,
        player_id: int,
    ) -> Optional[str]:
        """
        Return country name.
        """

        data = self.get_player_info(player_id)

        return (
            data.get("country")
            or data.get("team")
        )

    # --------------------------------------------------

    def get_role(
        self,
        player_id: int,
    ) -> Optional[str]:
        """
        Return playing role.
        """

        data = self.get_player_info(player_id)

        return (
            data.get("role")
            or data.get("playingRole")
        )

    # --------------------------------------------------

    def get_batting_average(
        self,
        player_id: int,
    ) -> Optional[Any]:
        """
        Return batting average.
        """

        data = self.get_batting_stats(player_id)

        return (
            data.get("average")
            or data.get("battingAverage")
        )

    # --------------------------------------------------

    def get_total_runs(
        self,
        player_id: int,
    ) -> Optional[Any]:
        """
        Return career runs.
        """

        data = self.get_batting_stats(player_id)

        return (
            data.get("runs")
            or data.get("totalRuns")
        )

    # --------------------------------------------------

    def get_total_wickets(
        self,
        player_id: int,
    ) -> Optional[Any]:
        """
        Return career wickets.
        """

        data = self.get_bowling_stats(player_id)

        return (
            data.get("wickets")
            or data.get("totalWickets")
        )

    # --------------------------------------------------

    def get_bowling_average(
        self,
        player_id: int,
    ) -> Optional[Any]:
        """
        Return bowling average.
        """

        data = self.get_bowling_stats(player_id)

        return (
            data.get("average")
            or data.get("bowlingAverage")
        )

    # --------------------------------------------------

    def get_player_summary(
        self,
        player_id: int,
    ) -> Dict[str, Any]:
        """
        Return summarized player information.
        """

        return {
            "player_id": player_id,
            "name": self.get_player_name(player_id),
            "country": self.get_country(player_id),
            "role": self.get_role(player_id),
            "runs": self.get_total_runs(player_id),
            "wickets": self.get_total_wickets(player_id),
            "batting_average": self.get_batting_average(player_id),
            "bowling_average": self.get_bowling_average(player_id),
        }

    # --------------------------------------------------

    def search_players(
        self,
        player_ids: List[int],
    ) -> List[Dict[str, Any]]:
        """
        Fetch summaries for multiple players.
        """

        players = []

        for player_id in player_ids:

            try:

                players.append(
                    self.get_player_summary(player_id)
                )

            except Exception as ex:

                logger.exception(ex)

        return players


# Singleton Instance

players_api = PlayersAPI()