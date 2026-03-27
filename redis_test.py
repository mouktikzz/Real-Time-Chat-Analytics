from redis_client import *

increment_total()
increment_spam()
add_sentiment(0.8)

print(get_metrics())
print(get_sentiments())

print("Hello")