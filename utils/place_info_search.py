import os
from langchain_tavily import TavilySearch

try:
    from langchain_google_community import GooglePlacesTool, GooglePlacesAPIWrapper
except ImportError:  # pragma: no cover
    GooglePlacesTool = None
    GooglePlacesAPIWrapper = None


class GooglePlaceSearchTool:
    def __init__(self, api_key: str | None):
        self.enabled = bool(api_key and str(api_key).strip())
        self.places_tool = None
        if self.enabled and GooglePlacesAPIWrapper is not None:
            self.places_wrapper = GooglePlacesAPIWrapper(gplaces_api_key=api_key)
            self.places_tool = GooglePlacesTool(api_wrapper=self.places_wrapper)

    def _run(self, query: str) -> str:
        if not self.places_tool:
            raise RuntimeError("Google Places API is not configured")
        return self.places_tool.run(query)

    def google_search_attractions(self, place: str) -> dict:
        """Searches for attractions in the specified place using GooglePlaces API."""
        return self._run(f"top attractive places in and around {place}")

    def google_search_restaurants(self, place: str) -> dict:
        """Searches for available restaurants in the specified place using GooglePlaces API."""
        return self._run(f"what are the top 10 restaurants and eateries in and around {place}?")

    def google_search_activity(self, place: str) -> dict:
        """Searches for popular activities in the specified place using GooglePlaces API."""
        return self._run(f"Activities in and around {place}")

    def google_search_transportation(self, place: str) -> dict:
        """Searches for available modes of transportation in the specified place using GooglePlaces API."""
        return self._run(f"What are the different modes of transportations available in {place}")


class TavilyPlaceSearchTool:
    def __init__(self):
        self.enabled = bool(os.environ.get("TAVILY_API_KEY", "").strip())

    def _search(self, query: str) -> str:
        if not self.enabled:
            return (
                "Tavily search is unavailable because TAVILY_API_KEY is not set. "
                "Please configure the key in your .env file."
            )
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": query})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return str(result)

    def tavily_search_attractions(self, place: str) -> dict:
        """Searches for attractions in the specified place using TavilySearch."""
        return self._search(f"top attractive places in and around {place}")

    def tavily_search_restaurants(self, place: str) -> dict:
        """Searches for available restaurants in the specified place using TavilySearch."""
        return self._search(f"what are the top 10 restaurants and eateries in and around {place}.")

    def tavily_search_activity(self, place: str) -> dict:
        """Searches for popular activities in the specified place using TavilySearch."""
        return self._search(f"activities in and around {place}")

    def tavily_search_transportation(self, place: str) -> dict:
        """Searches for available modes of transportation in the specified place using TavilySearch."""
        return self._search(f"What are the different modes of transportations available in {place}")
