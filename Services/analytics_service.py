"""
Services/analytics_service.py
------------------------------
Analytics queries for batting and bowling statistics.
"""

import logging
from Database.Repository import Repository

logger = logging.getLogger(__name__)


class AnalyticsService:
    def __init__(self):
        self.repo = Repository()

    def get_top_batsmen(self, limit: int = 10, format: str = "All Formats"):
        """Return top run-scorers from player_statistics."""
        query = """
            SELECT p.full_name       AS player_name,
                   t.team_name       AS team_name,
                   ps.runs,
                   ps.batting_average AS batting_avg,
                   ps.matches,
                   ps.hundreds       AS centuries,
                   ps.fifties        AS half_centuries,
                   ps.strike_rate
            FROM player_statistics ps
            JOIN players p ON ps.player_id = p.player_id
            LEFT JOIN teams t ON p.team_id = t.team_id
            {where}
            ORDER BY ps.runs DESC
            LIMIT %s
        """
        if format and format != "All Formats":
            query = query.format(where="WHERE ps.format = %s")
            return self.repo.fetch_all(query, (format, limit))
        else:
            query = query.format(where="")
            return self.repo.fetch_all(query, (limit,))

    def get_top_bowlers(self, limit: int = 10, format: str = "All Formats"):
        """Return top wicket-takers from player_statistics."""
        query = """
            SELECT p.full_name        AS player_name,
                   t.team_name        AS team_name,
                   ps.wickets,
                   ps.bowling_average AS bowling_avg,
                   ps.economy        AS economy_rate,
                   ps.matches
            FROM player_statistics ps
            JOIN players p ON ps.player_id = p.player_id
            LEFT JOIN teams t ON p.team_id = t.team_id
            WHERE ps.wickets > 0
            {extra}
            ORDER BY ps.wickets DESC
            LIMIT %s
        """
        if format and format != "All Formats":
            query = query.format(extra="AND ps.format = %s")
            return self.repo.fetch_all(query, (format, limit))
        else:
            query = query.format(extra="")
            return self.repo.fetch_all(query, (limit,))
