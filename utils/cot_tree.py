# Class for rendering the Chain-of-Thought (CoT) Tree view
class CoTManager:
    def __init__(self):
        self.sessions = {"session_1" : {}}

    def add_node(self, session_id, node_id, query, response, research_term, research_papers):
        if session_id not in self.sessions:
            self.sessions[session_id] = {}
        self.sessions[session_id][node_id] = {
            "query": query,
            "response": response,
            "research_term" : research_term,
            "research_papers" : research_papers
        }

    def get_tree(self, session_id):
        return self.sessions.get(session_id, {})

    def list_sessions(self):
        return list(self.sessions.keys())
    
    def add_session(self, new_session_id):
        self.sessions[new_session_id] = {}