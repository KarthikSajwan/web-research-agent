# core/orchestrator.py

from tools.search_tool import SearchTool
from core.query_parser import parse_query
from core.synthesizer import synthesize

class Orchestrator:
    def __init__(self):
        self.search_tool = SearchTool()

    def run(self, raw_query: str) -> dict:
        # 1. Parse
        query = parse_query(raw_query)

        # 2. Search
        results = self.search_tool.search(query)

        # 3. Synthesize
        summary = synthesize(results)

        return {
            "query": query,
            "results": results,
            "summary": summary
        }
