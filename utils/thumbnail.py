import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv("LINK_PREVIEW_API_KEY")

# Fetch a thumbnail preview for a URL using the LinkPreview API
def get_thumbnail(url):
    try:
        response = requests.get(
            "https://api.linkpreview.net/",
            params={"key": api_key, "q": url}
        )
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    except Exception as e:
        return None