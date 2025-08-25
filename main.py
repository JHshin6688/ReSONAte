from fastapi import FastAPI
from utils.cot_tree import CoTManager
from pydantic import BaseModel
import uuid

from utils.perplexity_api import query_perplexity
from utils.perplexity_api import extract_topic
from utils.extract import extract_core_term
from utils.semantic_scholar import fetch_papers

app = FastAPI()

# Global CoT Manager
cot_manager = CoTManager()
session_counter = 2

class ResearchQuery(BaseModel):
    session_id: str
    query: str

# Define endpoint for retrieving all active sessions
@app.get("/sessions")
async def list_sessions():
    return {"active_sessions": cot_manager.list_sessions()}

# Define endpoint for creating a new session
@app.get("/create_session")
async def create_session():
    global session_counter
    new_session_id = f"session_{session_counter}"
    cot_manager.add_session(new_session_id)
    session_counter += 1
    return {"session_id": new_session_id}

# Define endpoint for query processing
@app.post("/query")
async def research_query(data: ResearchQuery):
    sonar_response = query_perplexity(data.query)
    topic = extract_topic(data.query)
    research_term = extract_core_term(topic.choices[0].message.content)
    node_id = str(uuid.uuid4())
    papers = fetch_papers(research_term)

    cot_manager.add_node(session_id=data.session_id, node_id=node_id, query=data.query, response=sonar_response,
                         research_term = research_term, research_papers = papers)

    return {
        "node_id": node_id,
        "response": sonar_response,
        "research_papers": papers,
        "cot_tree": cot_manager.get_tree(data.session_id),
        "research_term" : research_term
    }

# Define endpoint for retrieving CoT tree for current session
@app.get("/tree/{session_id}")
async def get_cot_tree(session_id: str):
    return {"cot_tree": cot_manager.get_tree(session_id)}