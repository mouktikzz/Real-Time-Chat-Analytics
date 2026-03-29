"""
Message processor for the Real-Time Chat Analytics System.
"""

from collections import deque
from typing import List, Dict, Any

from config import WINDOW_SIZE

class MessageProcessor:
    def __init__(self):
        self.messages = deque(maxlen=WINDOW_SIZE)

    def add_message(self, message: Dict[str, Any]):
        """Adds a new message to the sliding window."""
        # add_message({"user_id": 1, "message": "Hi!"})
        self.messages.append(message)

    def get_messages(self) -> List[Dict[str, Any]]:
        """Returns all messages in the current window."""
        # get_messages() -> [{"user_id": 1, "message": "Hi!"}, ...]
        return list(self.messages)
