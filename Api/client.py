"""
api/client.py

Reusable HTTP client for Cricbuzz RapidAPI.

Features
--------
- Session reuse
- Automatic retries
- Exponential backoff
- Timeout handling
- Logging
- JSON validation
- Custom exceptions
- Type hints
"""

from __future__ import annotations

import logging
from typing import Any, Dict, Optional

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from config import Config


# -------------------------------------------------------
# Logging Configuration
# -------------------------------------------------------

logger = logging.getLogger(__name__)


# -------------------------------------------------------
# Custom Exceptions
# -------------------------------------------------------

class CricbuzzAPIError(Exception):
    """Base exception for Cricbuzz API."""


class AuthenticationError(CricbuzzAPIError):
    """Raised when authentication fails."""


class RateLimitError(CricbuzzAPIError):
    """Raised when API rate limit is exceeded."""


class ResourceNotFound(CricbuzzAPIError):
    """Raised when endpoint returns 404."""


class ServerError(CricbuzzAPIError):
    """Raised when API server fails."""


# -------------------------------------------------------
# API Client
# -------------------------------------------------------

class APIClient:
    """
    Generic HTTP Client for Cricbuzz API.
    """

    DEFAULT_TIMEOUT = 30

    def __init__(self):

        self.base_url = Config.BASE_URL.rstrip("/")

        self.headers = {
            "x-rapidapi-key": Config.RAPIDAPI_KEY,
            "x-rapidapi-host": Config.RAPIDAPI_HOST,
            "Content-Type": "application/json"
        }

        self.session = self._create_session()

    # ---------------------------------------------------

    def _create_session(self) -> requests.Session:
        """
        Create requests session with retry strategy.
        """

        retry = Retry(
            total=5,
            backoff_factor=1,
            status_forcelist=[
                429,
                500,
                502,
                503,
                504
            ],
            allowed_methods=[
                "GET",
                "POST",
                "PUT",
                "DELETE"
            ],
        )

        adapter = HTTPAdapter(max_retries=retry)

        session = requests.Session()

        session.mount("https://", adapter)
        session.mount("http://", adapter)

        session.headers.update(self.headers)

        return session

    # ---------------------------------------------------

    def _handle_errors(self, response: requests.Response):

        if response.status_code == 401:
            raise AuthenticationError(
                "Invalid RapidAPI Key."
            )

        if response.status_code == 404:
            raise ResourceNotFound(
                "Requested resource not found."
            )

        if response.status_code == 429:
            raise RateLimitError(
                "RapidAPI rate limit exceeded."
            )

        if response.status_code >= 500:
            raise ServerError(
                f"Server Error ({response.status_code})"
            )

        response.raise_for_status()

    # ---------------------------------------------------

    def get(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:

        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        logger.info("GET %s", url)

        response = self.session.get(
            url,
            params=params,
            timeout=self.DEFAULT_TIMEOUT
        )

        self._handle_errors(response)

        return response.json()

    # ---------------------------------------------------

    def close(self):

        self.session.close()


# -------------------------------------------------------
# Singleton Client
# -------------------------------------------------------

client = APIClient()