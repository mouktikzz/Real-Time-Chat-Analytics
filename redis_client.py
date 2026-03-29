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
    try:
        r.incr("total_messages")
    except Exception as e:
        print(f"Error incrementing total_messages in Redis: {e}")

def increment_spam():
    try:
        r.incr("spam_count")
    except Exception as e:
        print(f"Error incrementing spam_count in Redis: {e}")

def get_metrics():
    try:
        return {
            "total": int(r.get("total_messages") or 0),
            "spam": int(r.get("spam_count") or 0),
        }
    except Exception as e:
        print(f"Error getting metrics from Redis: {e}")
        return {"error": str(e)}

def add_sentiment(score):
    try:
        r.lpush("sentiments", score)
        r.ltrim("sentiments", 0, 99)  # keep last 100
    except Exception as e:
        print(f"Error adding sentiment to Redis: {e}")

def get_sentiments():
    try:
        return [float(x) for x in r.lrange("sentiments", 0, 99)]
    except Exception as e:
        print(f"Error getting sentiments from Redis: {e}")
        return []

# try:
#     r.ping()
#     print("Cnnected to Redis")
# except Exception as e:
#     print("Redis connection failed:", e)