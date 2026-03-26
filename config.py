"""
Configuration settings for the Real-Time Chat Analytics System.
"""

# Message generation
MESSAGE_RATE = 1000  # messages per second

# Sliding window size for analytics
WINDOW_SIZE = 1000

# Top-K trending words to display
TOP_K_WORDS = 10

# Spam detection keywords
SPAM_KEYWORDS = ["buy now", "offer", "free", "subscribe", "win", "prize"]
