import redis

# Create Redis connection
r = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True  # returns strings instead of bytes
)

# Helper functions (clean usage)

def increment_total():
    r.incr("total_messages")

def increment_spam():
    r.incr("spam_count")

def get_metrics():
    return {
        "total": int(r.get("total_messages") or 0),
        "spam": int(r.get("spam_count") or 0),
    }

def add_sentiment(score):
    r.lpush("sentiments", score)
    r.ltrim("sentiments", 0, 99)  # keep last 100

def get_sentiments():
    return [float(x) for x in r.lrange("sentiments", 0, 99)]

# try:
#     r.ping()
#     print("Cnnected to Redis")
# except Exception as e:
#     print("Redis connection failed:", e)