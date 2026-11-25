"""
API Module
----------
Cricbuzz API integration for fetching cricket data.
"""

from .client import APIClient
from .matches import MatchesAPI
from .players import PlayersAPI
from .rankings import RankingsAPI

# Create alias for backward compatibility
CricbuzzAPIClient = APIClient

__all__ = ['APIClient', 'CricbuzzAPIClient', 'MatchesAPI', 'PlayersAPI', 'RankingsAPI']
