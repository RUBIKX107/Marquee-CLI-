import requests
import os
from dotenv import load_dotenv

load_dotenv()

TMDB_API_KEY = os.getenv("9d4c88f18ff58d34ed793ca814761b68")

def search_tmdb_movies(query):
    """
    Search for movies using the TMDb API.
    """
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": "9d4c88f18ff58d34ed793ca814761b68", # Replace this!
        "query": query
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        results = response.json().get('results', [])
        # Just return the top 3 titles for now to keep it simple
        return [f"{m['title']} ({m['release_date'][:4]})" for m in results[:3]]
    return "Could not find any movies."

# Test it!
# print(search_tmdb_movies("Inception"))
