"""
Message consumer for the Real-Time Chat Analytics System.
"""

import asyncio
from typing import Dict, Any

from processor import MessageProcessor
from analytics import analyze_sentiment, is_spam
from redis_client import increment_total, increment_spam, add_sentiment

async def consumer(queue: asyncio.Queue, processor: MessageProcessor):
    """Consumes messages from the queue and performs analytics."""
    while True:
        msg = await queue.get()
        
        processor.add_message(msg)
        
        # Perform analytics
        msg["sentiment"] = analyze_sentiment(msg["message"])
        msg["is_spam"] = is_spam(msg["message"])
        
        # Store in Redis
        increment_total()
        if msg["is_spam"]:
            increment_spam()
        
        add_sentiment(msg["sentiment"])

        queue.task_done()
