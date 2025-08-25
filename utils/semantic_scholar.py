import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("SEMANTIC_SCHOLAR_API_KEY")

# Retrieve the top 5 research papers on a given topic (since 2023) using the Semantic Scholar API and key research terms
def fetch_papers(keywords: str):
    research_papers = []
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={keywords}&year=2023-"
    query_params = {"fields": "title,year,url"}
    headers = {"x-api-key": api_key}

    response = requests.get(url=url, params=query_params, headers=headers)

    if response.ok:
        papers = response.json().get("data", [])

        if papers:
            for i in range(5):
                paper = papers[i]
                research_papers.append({
                    "title": paper.get("title"),
                    "year": paper.get("year"),
                    "url": paper.get("url")
                })
    return research_papers