import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import streamlit as st
import time
import asyncio
import threading

from producer import producer
from consumer import consumer
from processor import MessageProcessor
from ui_components import update_metrics_ui, update_charts


@st.cache_resource
def get_engine():
    queue = asyncio.Queue()
    processor = MessageProcessor()

    def run_async_loop():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        loop.create_task(producer(queue))
        loop.create_task(consumer(queue, processor))

        loop.run_forever()

    thread = threading.Thread(target=run_async_loop, daemon=True)
    thread.start()

    return processor


def main():
    st.set_page_config(page_title="Chat Analytics Dashboard", layout="wide")
    st.title("🚀 Real-Time Chat Analytics System")

    processor = get_engine()

    col1, col2, col3 = st.columns(3)
    total_msg_metric = col1.empty()
    spam_count_metric = col2.empty()
    spam_pct_metric = col3.empty()

    chart_col1, chart_col2 = st.columns(2)
    with chart_col1:
        st.subheader("🔥 Top Trending Words")
        trending_words_chart = st.empty()
    with chart_col2:
        st.subheader("😊 Sentiment Analysis (Recent)")
        sentiment_chart = st.empty()

    while True:
        messages = processor.get_messages()[-500:]

        update_metrics_ui(total_msg_metric, spam_count_metric, spam_pct_metric)
        update_charts(messages, trending_words_chart, sentiment_chart)

        time.sleep(1)


if __name__ == "__main__":
    main()