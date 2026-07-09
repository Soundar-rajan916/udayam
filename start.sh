#!/bin/bash

# Start FastAPI backend in the background
# It runs on localhost so only Streamlit can talk to it
uvicorn main:app --host 127.0.0.1 --port 8000 &

# Start Streamlit frontend in the foreground
# It binds to the PORT provided by Render (default 10000)
export API_URL="http://127.0.0.1:8000/verify"
streamlit run frontend.py --server.port "${PORT:-10000}" --server.address 0.0.0.0
