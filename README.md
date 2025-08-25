# ReSONAte: Your Sonar for Smarter Research

ReSONAte is a web-based AI research assistant, built with **Streamlit** and **FastAPI**, that inspires curiosity and supports knowledge exploration.
ReSONAte helps users dive deeper into relevant topics and stay organized throughout their research journey.  



## Features

### QA View
- **In-depth Answers**: The **Perplexity Sonar-Pro API** generates detailed answers based on the user query.
- **Citations**: Citations are enriched with visual thumbnails using the **LinkPreview API**.
- **Relevant Papers**: From the user query, the **Perplexity Sonar API** produces a concise answer highlighting key research topics. These topics are refined with **KeyBERT** to extract precise terms, which are then used to retrieve relevant publications via the **Semantic Scholar API**.

### CoT (Chain-of-Thought) Tree View
- **Visual Query Map**: Queries are visualized as a directed graph using **Graphviz**.
- **Session-Based Interaction History**: Users can click on past queries to revisit the corresponding answers and research papers, helping them refine research direction.

## Installation

### 1. Clone the Repository
After cloning, move into the **ReSONAte** directory to proceed with setup and usage.
```
git clone https://github.com/JHshin6688/ReSONAte.git
cd ReSONAte
```
### 2. Set Up the Environment
Install required Python packages:
```
pip install -r requirements.txt
```
### 3. Add Your API Key
Create a .env file in the project root and add your API keys:
```
PERPLEXITY_API_KEY=your_perplexity_api_key_here
LINK_PREVIEW_API_KEY="your-link-preview-key-here"
SEMANTIC_SCHOLAR_API_KEY="your-semantic-scholar-key-here"
```

### 4. Running the App
To start ReSONAte, run the following commands in two separate terminals:
```
uvicorn main:app --reload
streamlit run app.py
```
Make sure both processes are running for ReSONAte to work properly.


## How to use
1. **Start with QA View**: From the main page, select QA View and ask any research question.
2. **Get In-Depth Responses**: ReSONAte will generate a detailed answer, including citations and links to relevant research papers.
3. **Ask Follow-Up Questions**: Feel free to continue the conversation with as many follow-up questions as you'd like.
4. **Track Your Research Journey**: Switch to the CoT Tree View to visualize the sequence of your queries and explore how your ideas have evolved.
5. **Explore New Topics**: To begin research on a different topic, create a new session using the sidebar. Your previous sessions will remain saved and accessible.