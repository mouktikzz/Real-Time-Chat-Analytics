# Real-Time Chat Analytics System

This project is a production-quality Python application that simulates and processes high-throughput chat message streams in real-time. It uses an asynchronous producer-consumer architecture, Redis for persistence, and provides a FastAPI backend alongside a Streamlit dashboard for live visualization.

## Architecture

The system is composed of several modular components:

- **`producer.py`**: Generates simulated chat messages and puts them into an `asyncio.Queue`.
- **`consumer.py`**: Retrieves messages from the queue, performs analytics, and stores results in Redis.
- **`processor.py`**: Maintains a sliding window of recent messages for trending word analysis.
- **`analytics.py`**: Core logic for trending words, sentiment scoring (VADER), and spam detection.
- **`redis_client.py`**: Abstraction layer for Redis interactions (metrics and sentiment history).
- **`api/main.py`**: FastAPI server providing endpoints for real-time analytics data.
- **`dashboard/dashboard.py`**: Streamlit application for visualizing analytics.
- **`config.py`**: Centralized configuration for message rates, window sizes, and keywords.

## Features

- **High-Throughput Processing**: Built with `asyncio` to handle thousands of messages per second.
- **Persistence with Redis**: All analytics (total messages, spam count, recent sentiment) are stored in Redis.
- **RESTful API**: FastAPI endpoints to query live metrics and sentiment history.
- **Trending Words**: Identifies the top-K most frequent words in the chat stream.
- **Sentiment Analysis**: Real-time sentiment scoring using `vaderSentiment`.
- **Live Dashboard**: A responsive Streamlit dashboard with real-time updates.

## Tech Stack

- **Python 3.10+**
- **Asyncio**: For high-concurrency message processing.
- **Redis**: For real-time data storage and persistence.
- **FastAPI**: For the analytics REST API.
- **Streamlit**: For the interactive visualization dashboard.
- **vaderSentiment**: For automated sentiment analysis.

## Prerequisites

- **Redis**: Ensure you have Redis installed and running on `localhost:6379`.

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mouktikzz/Real-Time-Chat-Analytics
   cd chat-analytics
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Dashboard (and Engine):**
   ```bash
   python dashboard/dashboard.py
   ```
   This will start the message producer/consumer engine and launch the Streamlit dashboard.

4. **Run the API (Optional):**
   ```bash
   uvicorn api.main:app --reload
   ```
   The API will be available at `http://localhost:8000`.

## API Endpoints

- `GET /metrics`: Returns total message count and spam count.
- `GET /sentiments`: Returns the history of recent sentiment scores.
- `GET /`: Health check and status.

## Dashboard Visualization

The dashboard provides:
- **Real-time Metrics**: Total processed messages, spam count, and spam percentage.
- **Trending Words Chart**: Bar chart of the most frequent words.
- **Sentiment Trend**: Line chart of recent message sentiments.
