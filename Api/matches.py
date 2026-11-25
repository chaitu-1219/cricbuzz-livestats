"""
api/matches.py

Match-related API wrapper for Cricbuzz RapidAPI.

Author : Your Name
Project: Cricbuzz LiveStats

Features
--------
✓ Live Matches
✓ Upcoming Matches
✓ Recent Matches
✓ Match List
✓ Match Details
✓ Scorecard
✓ Commentary
✓ Overs
✓ Team Details

PEP8 Compliant
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional

from Api.client import client

logger = logging.getLogger(__name__)


class MatchesAPI:
    """
    Wrapper class for all match endpoints.
    """

    # ----------------------------
    # Endpoint Constants
    # ----------------------------

    LIVE = "matches/v1/live"

    UPCOMING = "matches/v1/upcoming"

    RECENT = "matches/v1/recent"

    MATCH_LIST = "matches/list"

    MATCH_INFO = "matches/get-info"

    TEAM_INFO = "matches/get-team"

    COMMENTARY = "matches/get-commentaries"

    COMMENTARY_V2 = "matches/get-commentaries-v2"

    OVERS = "matches/get-overs"

    SCORECARD = "matches/get-scorecard"

    SCORECARD_V2 = "matches/get-scorecard-v2"

    # ----------------------------

    def get_live_matches(self) -> Dict[str, Any]:
        """
        Fetch all live matches.
        """
        logger.info("Fetching live matches")
        return client.get(self.LIVE)

    # ----------------------------

    def get_upcoming_matches(self) -> Dict[str, Any]:
        """
        Fetch upcoming matches.
        """
        logger.info("Fetching upcoming matches")
        return client.get(self.UPCOMING)

    # ----------------------------

    def get_recent_matches(self) -> Dict[str, Any]:
        """
        Fetch recently completed matches.
        """
        logger.info("Fetching recent matches")
        return client.get(self.RECENT)

    # ----------------------------

    def get_match_list(
        self,
        series_id: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Fetch list of matches.
        """

        params = {}

        if series_id:
            params["seriesId"] = series_id

        return client.get(
            self.MATCH_LIST,
            params=params
        )

    # ----------------------------

    def get_match_info(
        self,
        match_id: int,
    ) -> Dict[str, Any]:

        return client.get(
            self.MATCH_INFO,
            params={
                "matchId": match_id
            },
        )

    # ----------------------------

    def get_team_info(
        self,
        match_id: int,
    ) -> Dict[str, Any]:

        return client.get(
            self.TEAM_INFO,
            params={
                "matchId": match_id
            },
        )

    # ----------------------------

    def get_scorecard(
        self,
        match_id: int,
    ) -> Dict[str, Any]:

        return client.get(
            self.SCORECARD,
            params={
                "matchId": match_id
            },
        )

    # ----------------------------

    def get_scorecard_v2(
        self,
        match_id: int,
    ) -> Dict[str, Any]:

        return client.get(
            self.SCORECARD_V2,
            params={
                "matchId": match_id
            },
        )

    # ----------------------------

    def get_commentary(
        self,
        match_id: int,
    ) -> Dict[str, Any]:

        return client.get(
            self.COMMENTARY,
            params={
                "matchId": match_id
            },
        )

    # ----------------------------

    def get_commentary_v2(
        self,
        match_id: int,
    ) -> Dict[str, Any]:

        return client.get(
            self.COMMENTARY_V2,
            params={
                "matchId": match_id
            },
        )

    # ----------------------------

    def get_overs(
        self,
        match_id: int,
    ) -> Dict[str, Any]:

        return client.get(
            self.OVERS,
            params={
                "matchId": match_id
            },
        )

    # ----------------------------
    # Helper Methods
    # ----------------------------

    def get_batsmen(
        self,
        match_id: int,
        innings: int = 1,
    ) -> List[Dict[str, Any]]:
        """
        Returns batting card of an innings.
        """

        data = self.get_scorecard_v2(match_id)

        scorecards = data.get("scorecard", [])

        if innings > len(scorecards):
            return []

        return scorecards[innings - 1].get(
            "batsman",
            [],
        )

    # ----------------------------

    def get_bowlers(
        self,
        match_id: int,
        innings: int = 1,
    ) -> List[Dict[str, Any]]:

        data = self.get_scorecard_v2(match_id)

        scorecards = data.get("scorecard", [])

        if innings > len(scorecards):
            return []

        return scorecards[innings - 1].get(
            "bowler",
            [],
        )

    # ----------------------------

    def get_match_status(
        self,
        match_id: int,
    ) -> str:

        data = self.get_scorecard_v2(match_id)

        return data.get("status", "")

    # ----------------------------

    def get_match_result(
        self,
        match_id: int,
    ) -> str:

        data = self.get_scorecard_v2(match_id)

        return data.get("status", "")


matches_api = MatchesAPI()