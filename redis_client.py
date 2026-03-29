import redis

# Create Redis connection
try:
    r = redis.Redis(
        host="localhost",
        port=6379,
        db=0,
        decode_responses=True  # returns strings instead of bytes
    )
except Exception as e:
    print(f"Error connecting to Redis: {e}")
    raise

# Helper functions (clean usage)

def increment_total():
    # increment_total() -> total_messages: 121
    try:
        r.incr("total_messages")
    except Exception as e:
        print(f"Error incrementing total_messages in Redis: {e}")

def increment_spam():
    # increment_spam() -> spam_count: 16
    try:
        r.incr("spam_count")
    except Exception as e:
        print(f"Error incrementing spam_count in Redis: {e}")

def get_metrics():
    # get_metrics() -> {"total": 120, "spam": 15}
    try:
        return {
            "total": int(r.get("total_messages") or 0),
            "spam": int(r.get("spam_count") or 0),
        }
    except Exception as e:
        print(f"Error getting metrics from Redis: {e}")
        return {"error": str(e)}

def add_sentiment(score):
    # add_sentiment(0.85) -> sentiments list: [0.85, 0.45, -0.2, ...]
    try:
        r.lpush("sentiments", score)
        r.ltrim("sentiments", 0, 99)  # keep last 100
    except Exception as e:
        print(f"Error adding sentiment to Redis: {e}")

def get_sentiments():
    # get_sentiments() -> [0.85, 0.45, -0.2, ...]
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