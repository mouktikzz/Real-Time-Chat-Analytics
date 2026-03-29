"""
Dashboard for the Real-Time Chat Analytics System.
"""

import streamlit as st
import pandas as pd
import time
import asyncio
import threading
import requests

from analytics import get_trending_words
from producer import producer
from consumer import consumer
from processor import MessageProcessor



@st.cache_resource
def get_engine():
    """Starts the producer and consumer in a background thread."""
    queue = asyncio.Queue()
    processor = MessageProcessor()

    def run_async_loop():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        # Add producer and consumer to the loop
        loop.create_task(producer(queue))
        loop.create_task(consumer(queue, processor))
        
        loop.run_forever()

    # Start the async loop in a daemon thread
    thread = threading.Thread(target=run_async_loop, daemon=True)
    thread.start()

    return processor

def main():
    st.set_page_config(page_title="Chat Analytics Dashboard", layout="wide")
    st.title("🚀 Real-Time Chat Analytics System")

    # Initialize or get the shared engine
    processor = get_engine()

    # Layout for metrics
    col1, col2, col3 = st.columns(3)
    total_msg_metric = col1.empty()
    spam_count_metric = col2.empty()
    spam_pct_metric = col3.empty()

    # Layout for charts
    chart_col1, chart_col2 = st.columns(2)
    with chart_col1:
        st.subheader("🔥 Top Trending Words")
        trending_words_chart = st.empty()
    with chart_col2:
        st.subheader("😊 Sentiment Analysis (Recent)")
        sentiment_chart = st.empty()

    # Real-time update loop
    while True:
        messages = processor.get_messages()[-500:]
        
        # Update metrics from Redis
        try:
            metrics = requests.get("http://127.0.0.1:8000/metrics", timeout=5).json()
        except:
            metrics = {"total": 0, "spam": 0}
        total = metrics["total"]
        spam = metrics["spam"]
        spam_pct = (spam / total * 100) if total > 0 else 0

        total_msg_metric.metric("Total Messages", f"{total:,}")
        spam_count_metric.metric("Spam Count", f"{spam:,}")
        spam_pct_metric.metric("Spam %", f"{spam_pct:.1f}%")

        if messages:
            # Update trending words
            trending = get_trending_words(messages)
            if trending:
                df_trending = pd.DataFrame(trending, columns=["Word", "Frequency"])
                trending_words_chart.bar_chart(df_trending.set_index("Word"))

            # Update sentiment chart from Redis
            try:
                sentiments = requests.get("http://127.0.0.1:8000/sentiments", timeout=5).json()["sentiments"]
            except:
                sentiments = []
            if sentiments:
                df_sentiment = pd.DataFrame(sentiments, columns=["Sentiment"])
                sentiment_chart.line_chart(df_sentiment)

        time.sleep(1) # Refresh every second

if __name__ == "__main__":
    main()
