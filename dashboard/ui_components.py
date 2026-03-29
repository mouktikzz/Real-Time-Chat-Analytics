import pandas as pd
from chat_analytics.analytics import get_trending_words
from chat_analytics.api_client import fetch_metrics, fetch_sentiments


def update_metrics_ui(total_msg_metric, spam_count_metric, spam_pct_metric):
    metrics = fetch_metrics()

    total = metrics["total"]
    spam = metrics["spam"]
    spam_pct = (spam / total * 100) if total > 0 else 0

    total_msg_metric.metric("Total Messages", f"{total:,}")
    spam_count_metric.metric("Spam Count", f"{spam:,}")
    spam_pct_metric.metric("Spam %", f"{spam_pct:.1f}%")


def update_charts(messages, trending_words_chart, sentiment_chart):
    if messages:
        trending = get_trending_words(messages)
        if trending:
            df_trending = pd.DataFrame(trending, columns=["Word", "Frequency"])
            trending_words_chart.bar_chart(df_trending.set_index("Word"))

    sentiments = fetch_sentiments()
    if sentiments:
        df_sentiment = pd.DataFrame(sentiments, columns=["Sentiment"])
        sentiment_chart.line_chart(df_sentiment)