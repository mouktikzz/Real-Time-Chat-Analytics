"""
Analytics functions for the Real-Time Chat Analytics System.
"""

import re
from collections import Counter
from typing import List, Dict, Any

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from config import TOP_K_WORDS, SPAM_KEYWORDS

analyzer = SentimentIntensityAnalyzer()

def get_trending_words(messages: List[Dict[str, Any]]) -> List[tuple[str, int]]:
    """Calculates top-K trending words from a list of messages."""
    text = " ".join([msg["message"] for msg in messages])
    words = re.findall(r'\w+', text.lower())
    return Counter(words).most_common(TOP_K_WORDS)

def analyze_sentiment(message: str) -> float:
    """Analyzes the sentiment of a message and returns the compound score."""
    return analyzer.polarity_scores(message)["compound"]

def is_spam(message: str) -> bool:
    """Checks if a message is spam based on keywords."""
    return any(keyword in message.lower() for keyword in SPAM_KEYWORDS)
