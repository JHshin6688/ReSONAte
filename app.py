import streamlit as st
import graphviz

from interface.components import (
    render_answer,
    render_citations,
    render_research_papers
)

from interface.api import (
    fetch_sessions,
    create_session,
    submit_query,
    get_cot_tree
)

# --- Main interface ---
st.set_page_config(layout="wide")
st.title("🧠 ReSONAte : AI Research Assistant")
st.sidebar.markdown("## Sessions")

# --- Session Handling ---
if "session_id" not in st.session_state:
    sessions = fetch_sessions()
    st.session_state["session_id"] = sessions[0] if sessions else None

if "page" not in st.session_state:
    st.session_state.page = "QA View"

session_list = fetch_sessions()
selected_session = st.sidebar.selectbox(
    "Select session",
    session_list + ["➕ Create new session"],
    index = session_list.index(st.session_state["session_id"]) if st.session_state["session_id"] in session_list else 0
)

if selected_session == "➕ Create new session":
    st.session_state["session_id"] = create_session()
    st.session_state["page"] = "QA View"
    st.sidebar.success(f"New session created: {st.session_state['session_id']}")
    st.rerun()
else:
    st.session_state["session_id"] = selected_session

session_id = st.session_state["session_id"]
st.sidebar.markdown(f"**Current Session ID:** `{session_id}`")

# --- Page Mode Toggle ---
page = st.radio(
    "View Mode", ["QA View", "CoT Tree View"],
    index=["QA View", "CoT Tree View"].index(st.session_state.page),
    horizontal=True, key="page"
)

# --- QA View ---
if page == "QA View":
    query = st.text_input("Enter your research question:", placeholder="What are the latest trends in AI for healthcare?")

    if st.button("Ask AI") and query:
        try:
            data = submit_query(session_id, query)
            message = data["response"]["choices"][0]["message"]["content"]
            citations = data["response"].get("citations", [])
            research_term = data["research_term"]
            papers = data["research_papers"]

            render_answer(message)
            render_citations(citations)
            render_research_papers(research_term, papers)

        except Exception as e:
            st.error(f"❌ Failed to fetch response: {e}")

# --- CoT Tree View ---
elif page == "CoT Tree View":
    st.markdown("### 🌳 Chain-of-Thought Tree")

    cot_tree = get_cot_tree(session_id)

    if not cot_tree:
        st.info("No questions asked in this session yet.")
    else:
        graph = graphviz.Digraph()
        graph.attr(fontsize="25")
        graph.attr('node', fontsize='15')
        graph.attr('edge', fontsize='1')

        node_map = {}
        previous_node = None

        for node in cot_tree.values():
            query = node["query"]
            graph.node(query)
            node_map[query] = (
                node["response"]["choices"][0]["message"]["content"],
                node["response"].get("citations", []),
                node["research_term"],
                node["research_papers"]
            )
            if previous_node:
                graph.edge(previous_node, query)
            previous_node = query

        st.graphviz_chart(graph)
        st.markdown("### 💬 Click a query from above tree to view details below.")

        clicked_query = st.selectbox("Select a query to view its answer", list(node_map.keys()), label_visibility="collapsed")

        if clicked_query:
            message, citations, research_term, papers = node_map[clicked_query]
            render_answer(message)
            render_citations(citations)
            render_research_papers(research_term, papers)