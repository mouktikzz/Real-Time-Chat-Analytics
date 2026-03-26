# Real-Time Chat Analytics System

This project is a production-quality Python application that simulates and processes high-throughput chat message streams in real-time. It uses an asynchronous producer-consumer architecture to handle over 10,000 messages per second, performing analytics for trending words, sentiment analysis, and spam detection. The results are displayed on a live-updating Streamlit dashboard.

## Architecture

The system is composed of the following modules:

- **`producer.py`**: Generates simulated chat messages and puts them into an `asyncio.Queue`.
- **`consumer.py`**: Retrieves messages from the queue and uses the `MessageProcessor` to perform analytics.
- **`processor.py`**: Maintains a sliding window of recent messages using `collections.deque`.
- **`analytics.py`**: Contains functions for calculating trending words, sentiment scores, and detecting spam.
- **`dashboard.py`**: A Streamlit application that visualizes the analytics in real-time.
- **`config.py`**: Centralized configuration for parameters like message rate, window size, and spam keywords.
- **`main.py`**: The main entry point that launches the producer, consumer, and Streamlit dashboard.

## Features

- **High-Throughput Processing**: Built with `asyncio` to handle thousands of messages per second.
- **Trending Words**: Identifies the top-K most frequent words in the chat stream.
- **Sentiment Analysis**: Calculates the sentiment of each message using `vaderSentiment`.
- **Spam Detection**: Flags messages containing spam-related keywords.
- **Live Dashboard**: Visualizes analytics using Streamlit with auto-refresh.

## Tech Stack

- Python 3.10+
- `asyncio` for asynchronous programming
- `Streamlit` for the web dashboard
- `vaderSentiment` for sentiment analysis
- `pandas` for data manipulation

## How to Run

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd chat-analytics
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python main.py
   ```

4. **View the dashboard:**
   Open your browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

## Example Output

The dashboard will display:

- A bar chart of the top trending words.
- A line chart showing the sentiment score over time.
- Metrics for total messages processed and spam count.
