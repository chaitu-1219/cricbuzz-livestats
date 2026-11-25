"""
Services/match_service.py
--------------------------
Business logic for live match data from the Cricbuzz API.
"""

import logging
from Api.matches import MatchesAPI

logger = logging.getLogger(__name__)


class MatchService:
    def __init__(self):
        self.api = MatchesAPI()

    def get_live_matches(self):
        """Fetch current live matches from Cricbuzz API."""
        return self.api.get_live_matches()

    def get_upcoming_matches(self):
        return self.api.get_upcoming_matches()

    def get_recent_matches(self):
        return self.api.get_recent_matches()

    def get_scorecard(self, match_id: int):
        return self.api.get_scorecard(match_id)
