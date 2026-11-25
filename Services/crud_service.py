"""
Services/crud_service.py
------------------------
CRUD operations on the players table.
"""

import logging
from Database.Repository import Repository

logger = logging.getLogger(__name__)


class CRUDService:
    def __init__(self):
        self.repo = Repository()

    # ------------------------------------------------------------------
    # CREATE
    # ------------------------------------------------------------------
    def create_player(self, data: dict):
        """
        Insert a new player row.
        data keys: player_name, country, playing_role, batting_style,
                   bowling_style, date_of_birth, jersey_number, is_active
        """
        # Resolve or create the team for the given country
        team_id = self._get_or_create_team(data.get("country", "Unknown"))

        query = """
            INSERT INTO players
                (full_name, team_id, role, batting_style, bowling_style)
            VALUES (%s, %s, %s, %s, %s)
        """
        params = (
            data.get("player_name"),
            team_id,
            data.get("playing_role"),
            data.get("batting_style"),
            data.get("bowling_style"),
        )
        return self.repo.execute(query, params)

    # ------------------------------------------------------------------
    # READ
    # ------------------------------------------------------------------
    def read_players(self, filters: dict = None):
        """
        Return a list of player dicts. Supports optional filters:
        player_name (LIKE), country (via team join), playing_role.
        """
        base_query = """
            SELECT p.player_id,
                   p.full_name  AS player_name,
                   t.team_name  AS country,
                   p.role       AS playing_role,
                   p.batting_style,
                   p.bowling_style,
                   1            AS is_active
            FROM players p
            LEFT JOIN teams t ON p.team_id = t.team_id
        """
        conditions = []
        params = []

        if filters:
            if filters.get("player_name"):
                conditions.append("p.full_name LIKE %s")
                params.append(f"%{filters['player_name']}%")
            if filters.get("country"):
                conditions.append("t.team_name = %s")
                params.append(filters["country"])
            if filters.get("playing_role"):
                conditions.append("p.role = %s")
                params.append(filters["playing_role"])

        if conditions:
            base_query += " WHERE " + " AND ".join(conditions)

        base_query += " ORDER BY p.full_name LIMIT 200"
        return self.repo.fetch_all(base_query, tuple(params) if params else None)

    # ------------------------------------------------------------------
    # UPDATE
    # ------------------------------------------------------------------
    def update_player(self, data: dict):
        query = """
            UPDATE players
            SET role          = %s,
                batting_style = %s,
                bowling_style = %s
            WHERE player_id = %s
        """
        params = (
            data.get("playing_role"),
            data.get("batting_style"),
            data.get("bowling_style"),
            data.get("player_id"),
        )
        return self.repo.execute(query, params)

    # ------------------------------------------------------------------
    # DELETE
    # ------------------------------------------------------------------
    def delete_player(self, player_id: int):
        # Remove dependent stats first to avoid FK constraint errors
        self.repo.execute(
            "DELETE FROM player_statistics WHERE player_id = %s",
            (player_id,)
        )
        return self.repo.execute(
            "DELETE FROM players WHERE player_id = %s",
            (player_id,)
        )

    # ------------------------------------------------------------------
    # Helper
    # ------------------------------------------------------------------
    def _get_or_create_team(self, country_name: str) -> int:
        row = self.repo.fetch_one(
            "SELECT team_id FROM teams WHERE team_name = %s",
            (country_name,)
        )
        if row:
            return row["team_id"]
        # Create a bare-bones team entry
        return self.repo.execute(
            "INSERT INTO teams (team_name) VALUES (%s)",
            (country_name,)
        )
