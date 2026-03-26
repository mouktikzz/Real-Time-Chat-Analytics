"""
Message producer for the Real-Time Chat Analytics System.
"""

import asyncio
import random
import time
from typing import Dict, Any

from config import MESSAGE_RATE

async def producer(queue: asyncio.Queue):
    """Generates and puts chat messages into the queue."""
    message_samples = [
        "Hello everyone!",
        "This is a great discussion.",
        "I agree with that point.",
        "Can you explain that further?",
        "Let's talk about the new features.",
        "buy now, special offer!",
        "free prize, click here!",
    ]

    while True:
        user_id = random.randint(1, 1000)
        message = random.choice(message_samples)
        timestamp = time.time()

        msg: Dict[str, Any] = {
            "user_id": user_id,
            "timestamp": timestamp,
            "message": message,
        }

        await queue.put(msg)
        await asyncio.sleep(1 / MESSAGE_RATE)
