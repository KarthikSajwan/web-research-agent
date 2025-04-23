# core/synthesizer.py

from typing import List, Dict

def synthesize(results: List[Dict]) -> str:
    """
    Stub summarizer. 
    Later feed `results` to your AI model for a proper summary.
    """
    count = len(results)
    return f"Found {count} result{'s' if count != 1 else ''}."
