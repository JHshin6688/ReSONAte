import requests
import os
import sys
sys.path.append(os.path.dirname(__file__))
from config import BACKEND_URL

# Send a request to retrieve all active sessions
def fetch_sessions():
    resp = requests.get(f"{BACKEND_URL}/sessions")
    resp.raise_for_status()
    return resp.json()["active_sessions"]

# Send a request to create a new session
def create_session():
    resp = requests.get(f"{BACKEND_URL}/create_session")
    resp.raise_for_status()
    return resp.json()["session_id"]

# Send a request to process the user's query
def submit_query(session_id, query):
    payload = {
        "session_id": session_id,
        "query": query,
    }
    resp = requests.post(f"{BACKEND_URL}/query", json=payload)
    resp.raise_for_status()
    return resp.json()

# Send a request to retrieve the CoT tree for the current session
def get_cot_tree(session_id):
    resp = requests.get(f"{BACKEND_URL}/tree/{session_id}")
    resp.raise_for_status()
    return resp.json()["cot_tree"]