"""
Message consumer for the Real-Time Chat Analytics System.
"""

import asyncio

from processor import MessageProcessor
from analytics import analyze_sentiment, is_spam
from redis_client import increment_total, increment_spam, add_sentiment

async def consumer(queue: asyncio.Queue, processor: MessageProcessor):
    """Consumes messages from the queue and performs analytics."""
    while True:
        try:
            # {"user_id": "23", "timestamp": 1234567890, "message": "I love this product!"}
            msg = await queue.get()
            
            # processor now holds the message for batching or further processing
            processor.add_message(msg)
            
            # Perform analytics
            # sentiment: "I love this product!" -> 0.85 (positive)
            msg["sentiment"] = analyze_sentiment(msg["message"])
            # {"user_id": "23", "timestamp": 1234567890, "message": "I love this product!", "sentiment": 0.85}
            
            # spam check: "I love this product!" -> False (not spam)
            msg["is_spam"] = is_spam(msg["message"])
            # {"user_id": "23", "timestamp": 1234567890, "message": "I love this product!", "sentiment": 0.85, "is_spam": False}
            
            # Store in Redis
            try:
                increment_total()
            except Exception as e:
                print(f"Error incrementing total_messages in Redis: {e}")
            
            if msg["is_spam"]:
                try:
                    increment_spam()
                except Exception as e:
                    print(f"Error incrementing spam_count in Redis: {e}")
            
            try:
                add_sentiment(msg["sentiment"])
            except Exception as e:
                print(f"Error adding sentiment to Redis: {e}")
        except Exception as e:
            print(f"Error processing message: {e}")
        finally:
            queue.task_done()
