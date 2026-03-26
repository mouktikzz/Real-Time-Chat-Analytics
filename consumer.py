"""
Message consumer for the Real-Time Chat Analytics System.
"""

import asyncio
from typing import Dict, Any

from processor import MessageProcessor
from analytics import analyze_sentiment, is_spam

async def consumer(
    queue: asyncio.Queue,
    processor: MessageProcessor,
    analytics_results: Dict[str, Any]
):
    """Consumes messages from the queue and performs analytics."""
    while True:
        msg = await queue.get()
        
        processor.add_message(msg)
        
        # Perform analytics
        msg["sentiment"] = analyze_sentiment(msg["message"])
        msg["is_spam"] = is_spam(msg["message"])
        
        # Update shared results
        analytics_results["total_messages"] += 1
        if msg["is_spam"]:
            analytics_results["spam_count"] += 1
        
        # To keep the example simple, we won't store historical sentiment.
        # A real application might store this for time-series analysis.
        
        queue.task_done()
