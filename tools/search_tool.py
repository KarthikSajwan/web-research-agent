# tools/search_tool.py

import os
from typing import List, Dict

class SearchTool:
    def __init__(self):
        self.api_key = os.getenv("SEARCH_API_KEY")
        if not self.api_key:
            raise RuntimeError("SEARCH_API_KEY environment variable not set")

    def search(self, query: str) -> List[Dict]:
        """
        Stub implementation.
        Replace with a real API call to SerpAPI, Bing Search, etc.
        """
        # TODO: integrate real search API here
        return [
            {
                "title": f"Dummy result for '{query}'",
                "link": "https://example.com",
                "snippet": "This is a placeholder snippet."
            }
        ]
