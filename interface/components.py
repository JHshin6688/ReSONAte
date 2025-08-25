import streamlit as st
import sys
import re
import os
from urllib.parse import urlparse
from utils.thumbnail import get_thumbnail
sys.path.append(os.path.dirname(__file__))
from config import WHITE_PIXEL

# Render the response from Perplexity Sonar on the interface
def render_answer(message):
    message_link = re.sub(r'\[(\d+)\]', r'<a href="#cite-\1" style="color: red;">[\1]</a>', message)
    st.markdown("## 🧾 Answer\n" + message_link, unsafe_allow_html=True)
    st.markdown("\n")

# Display citations by rendering visual thumbnails on the interface
def render_citations(citations):
    if citations:
        st.markdown("## 📚 Citations")
        cols = st.columns(len(citations))
        for i, (col, url) in enumerate(zip(cols, citations), start=1):
            preview = get_thumbnail(url)
            image_src = preview['image'] if preview and preview.get('image') else WHITE_PIXEL
            title = preview['title'] if preview and preview.get('title') else urlparse(url).netloc
            with col:
                st.markdown(f"""
                    <div id=\"cite-{i}\" style=\"border: 1px solid #ccc; padding: 10px; border-radius: 8px; background-color: #fafafa;\">
                        <a href=\"{url}\" target=\"_blank\" style=\"text-decoration: none; color: black;\">
                            <div style=\"width: 100%; aspect-ratio: 5 / 3; background-color: white; border-radius: 4px; overflow: hidden;\">
                                <img src=\"{image_src}\" alt=\"Preview Image\" style=\"width: 100%; height: 100%; object-fit: cover;\" />
                            </div>
                            <h4 style=\"font-size: 0.9rem; margin-top: 8px;\">[{i}] {title}</h4>
                        </a>
                    </div>
                """, unsafe_allow_html=True)
        st.markdown("\n")

# Render relevant research terms and links to recent related papers
def render_research_papers(research_term, papers):
    st.markdown(f"""
        <h2>📝 Research Papers on 
            <span style='color:#ff4b4b; font-weight:bold;'>{research_term}</span>
        </h2>
    """, unsafe_allow_html=True)

    for c in papers:
        st.markdown(f"- [{c['title']}]({c['url']}) ({c['year']})")