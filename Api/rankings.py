"""
api/rankings.py

ICC Rankings API Wrapper for Cricbuzz RapidAPI.

Author: Your Name
Project: Cricbuzz LiveStats

Features
--------
✓ Team Rankings
✓ Batting Rankings
✓ Bowling Rankings
✓ All-rounder Rankings
✓ Test / ODI / T20I Formats
✓ Logging
✓ Error Handling
✓ Type Hints
✓ Helper Functions
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional

from Api.client import client

logger = logging.getLogger(__name__)


class RankingsAPI:
    """
    Wrapper class for ICC ranking endpoints.
    """

    TEAM_RANKINGS = "rankings/get-team"
    BATTING_RANKINGS = "rankings/get-batting"
    BOWLING_RANKINGS = "rankings/get-bowling"
    ALL_ROUNDER_RANKINGS = "rankings/get-all-rounder"

    # --------------------------------------------
    # Team Rankings
    # --------------------------------------------

    def get_team_rankings(
        self,
        format_type: str = "test"
    ) -> Dict[str, Any]:
        """
        Fetch ICC Team Rankings.

        format_type:
            test
            odi
            t20
        """

        logger.info(
            "Fetching Team Rankings (%s)",
            format_type,
        )

        return client.get(
            self.TEAM_RANKINGS,
            params={
                "formatType": format_type
            }
        )

    # --------------------------------------------
    # Batting Rankings
    # --------------------------------------------

    def get_batting_rankings(
        self,
        format_type: str = "test"
    ) -> Dict[str, Any]:

        logger.info(
            "Fetching Batting Rankings (%s)",
            format_type,
        )

        return client.get(
            self.BATTING_RANKINGS,
            params={
                "formatType": format_type
            }
        )

    # --------------------------------------------
    # Bowling Rankings
    # --------------------------------------------

    def get_bowling_rankings(
        self,
        format_type: str = "test"
    ) -> Dict[str, Any]:

        logger.info(
            "Fetching Bowling Rankings (%s)",
            format_type,
        )

        return client.get(
            self.BOWLING_RANKINGS,
            params={
                "formatType": format_type
            }
        )

    # --------------------------------------------
    # All-Rounder Rankings
    # --------------------------------------------

    def get_all_rounder_rankings(
        self,
        format_type: str = "test"
    ) -> Dict[str, Any]:

        logger.info(
            "Fetching All-Rounder Rankings (%s)",
            format_type,
        )

        return client.get(
            self.ALL_ROUNDER_RANKINGS,
            params={
                "formatType": format_type
            }
        )

    # --------------------------------------------
    # Helper Methods
    # --------------------------------------------

    @staticmethod
    def _extract_rankings(
        response: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """
        Extract ranking list from API response.
        """

        if not response:
            return []

        for key in (
            "rank",
            "rankings",
            "ranking",
            "list",
            "data",
        ):
            value = response.get(key)
            if isinstance(value, list):
                return value

        return []

    def get_top_teams(
        self,
        format_type: str = "test",
        limit: int = 10
    ) -> List[Dict[str, Any]]:
        """
        Return top-ranked teams.
        """

        data = self.get_team_rankings(format_type)

        rankings = self._extract_rankings(data)

        return rankings[:limit]

    def get_top_batsmen(
        self,
        format_type: str = "test",
        limit: int = 10
    ) -> List[Dict[str, Any]]:

        data = self.get_batting_rankings(format_type)

        rankings = self._extract_rankings(data)

        return rankings[:limit]

    def get_top_bowlers(
        self,
        format_type: str = "test",
        limit: int = 10
    ) -> List[Dict[str, Any]]:

        data = self.get_bowling_rankings(format_type)

        rankings = self._extract_rankings(data)

        return rankings[:limit]

    def get_top_all_rounders(
        self,
        format_type: str = "test",
        limit: int = 10
    ) -> List[Dict[str, Any]]:

        data = self.get_all_rounder_rankings(format_type)

        rankings = self._extract_rankings(data)

        return rankings[:limit]

    # --------------------------------------------
    # Summary Method
    # --------------------------------------------

    def get_ranking_summary(
        self,
        format_type: str = "test"
    ) -> Dict[str, Any]:
        """
        Fetch all ranking categories.
        """

        return {
            "teams": self.get_top_teams(format_type),
            "batting": self.get_top_batsmen(format_type),
            "bowling": self.get_top_bowlers(format_type),
            "all_rounders": self.get_top_all_rounders(format_type),
        }


# Note: instantiate lazily, not at import time