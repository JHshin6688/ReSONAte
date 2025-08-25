import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Generate a detailed response to the user's query using Perplexity Sonar-Pro
def query_perplexity(query: str) -> str:
    api_key = os.getenv("PERPLEXITY_API_KEY")

    messages = [
        {
            "role": "system",
            "content": (
                "You are an artificial intelligence assistant and you need to "
                "engage in a helpful, detailed, polite conversation with a user."
                "If the query does not mention any specific research topics, suggest some of the most popular ones instead."
            ),
        },
        {   
            "role": "user",
            "content": (
                query
            ),
        },
    ]

    client = OpenAI(api_key=api_key, base_url="https://api.perplexity.ai")

    response = client.chat.completions.create(
        model="sonar-pro",
        messages=messages,
    )

    return response

# Provide a concise answer by identifying a key research term from the user's query using Perplexity Sonar
def extract_topic(query : str)-> str:
    api_key = os.getenv("PERPLEXITY_API_KEY")

    messages = [
        {
            "role": "system",
            "content": (
                "You are an artificial intelligence assistant and you need to extract one research term relevant to the user query."
                "If the query does not mention any specific research topics, suggest some of the most popular ones instead."
                "Please provide your answer in only one sentence and remove anything else."
            ),
        },
        {   
            "role": "user",
            "content": (
                query
            ),
        },
    ]

    client = OpenAI(api_key=api_key, base_url="https://api.perplexity.ai")

    response = client.chat.completions.create(
        model="sonar",
        messages=messages,
    )

    return response